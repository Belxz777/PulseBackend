
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from essential.models import JobTitle, Project, User
from essential.serializer import JobTitleSerializer, UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
import jwt,datetime
def index(request):
    return HttpResponse("Works Like ")


@api_view(['GET', 'POST', 'DELETE'])
def usersManagingbyId(request,id):
    if request.method == 'GET':
        user = User.objects.all().filter(id = id)
        user_serializer = UsersSerializer(user[0])
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=200)
        return JsonResponse(user_serializer.errors, status=400)
    

class RegisterView(APIView):
  def post(self,request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)
        
class LoginView(APIView):
    def post(self, request):
       data = request.data
       login = data['login']
       password = data['password']
       user = User.objects.filter(login=login).first()
       if user is None:
        raise AuthenticationFailed('Нету такого пользователя')
       if not user.password == password:
        raise AuthenticationFailed('Неверный пароль')
       payload = {
        'user': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
         'iat':datetime.datetime.utcnow()
    }
       token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
       response  = Response()
       response.set_cookie(key='jwt', value=token, httponly=True)
       response.data ={
           'message': 'Успешно логинизировлись',
           'token': token
       }
       return response

class UserView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if token is None:
            raise AuthenticationFailed({'message': 'Ты не аутетифицирован '}, status=401)
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Токен истек', status=401)
        user = User.objects.filter(id=payload['user']).first()
        serialize = UsersSerializer(user)
        return Response({'message': 'Ты аутетифицирован','token':token,'userData':serialize.data})





@api_view(['GET', 'POST', 'DELETE'])
def getJobTitleById(request,id):
    job = JobTitle.objects.all().filter(id = id)
    if request.method == 'GET':
        try:
            job_serializer = JobTitleSerializer(job[0])
            return JsonResponse(job_serializer.data, safe=False)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The job_title does not exist'}, status=404)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        job_serializer = JobTitleSerializer(data=user_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse(job_serializer.data, status=200)
        return JsonResponse(job_serializer.errors, status=400)
@api_view(['GET', 'POST', 'DELETE'])
def getJobTitle(request):
    job = JobTitle.objects.all()
    if request.method == 'GET':
        try:
            job_serializer = JobTitleSerializer(job[0])
            return JsonResponse(job_serializer.data, safe=False)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The job_title does not exist'}, status=404)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        job_serializer = JobTitleSerializer(data=user_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse(job_serializer.data, status=200)
        return JsonResponse(job_serializer.errors, status=400)


