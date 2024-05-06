from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
from .basic_comands import db_get

@api_view(['GET'])
def department_report(request,department_id):
    if request.method == 'GET':

        user_with_task = dict()
        users = User.objects.all().filter(department_id=department_id)
        
        for i in users:
            user_with_task[str(i.id)] = []
        
        for i in users:
            p = UserWIthTask.objects.all().filter(user_id = i.id)
            for j in p:
                s = UserWithTaskSerializer(j)
                user_with_task[str(i.id)].append(j)

        print(user_with_task)

