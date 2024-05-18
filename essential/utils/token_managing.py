from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

import jwt,datetime

from essential.utils.basic_comands import db_get

from ..models import User
from ..serializer import UsersSerializer
class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        login = data['login']
        password = data['password']
        user = User.objects.filter(login=login).first()
        
        print(user)
        if user is None:
            raise AuthenticationFailed('Нету такого пользователя')
        if not user.password == password:
            raise AuthenticationFailed('Неверный пароль')
        
        payload = {
            'user': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'Успешно логинизировлись',
            'token': token,
        }
        return response 


class UserView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if token is None:
            raise AuthenticationFailed({'message': 'Ты не аутетифицирован '})
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Токен истек')
        user = User.objects.filter(id=payload['user']).first()
        serialize = UsersSerializer(user)
        return Response({'message': 'Ты аутетифицирован', 'token': token, 'userData': serialize.data})


@api_view(['POST'])
def refresh_token(request):
    data = request.data
    token = data['token']
    try:
        payload = jwt.decode(token, "secret", algorithms=['HS256'])
        exp_time = datetime.datetime.fromtimestamp(payload['exp'])
        now = datetime.datetime.now()
        if now < exp_time:
            return Response({'message': 'Токен не истек'}, status=200)
        else:
            new_payload = {'exp': datetime.datetime.now() + datetime.timedelta(days=10)}
            new_token = jwt.encode(new_payload, 'secret', algorithm='HS256')
            return Response({'message': 'Токен истек, но был обновлен', 'token': new_token.decode('utf-8')}, status=200)

    except jwt.exceptions.DecodeError:
        return None