
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
from .basic_comands import db_get, db_create, db_update

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_managing(request, id):

    if request.method == 'GET':
        user = User.objects.all().filter(id=id)
        return db_get(user, UsersSerializer, User)

    elif request.method == 'POST':
        return db_create(request, UsersSerializer)

    elif request.method == 'PUT':
        return db_create(request, UsersSerializer, id)


@api_view(['GET', 'POST', 'DELETE'])
def job_title_managing(request, id):

    if request.method == 'GET':
        job = JobTitle.objects.all().filter(id=id)
        return db_get(job, JobTitleSerializer, JobTitle)

    elif request.method == 'POST':
        return db_create(request, JobTitleSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def project_managing(request, id):
    project = Project.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(project, ProjectSerializer, Project)

    elif request.method == 'POST':
        return db_create(request, ProjectSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def task_managing(request, id):
    task = Task.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(task, TaskSerializer, Task)

    elif request.method == 'POST':
        return db_create(request, TaskSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def user_with_task_managing(request, id):
    user_with_task = UserWithTask.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)

    elif request.method == 'POST':
        return db_create(request, UserWithTaskSerializer)




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
        return Response({'message': 'Ты аутетифицирован','token':token,'userData':serialize.data})

@api_view([ 'POST'])
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



