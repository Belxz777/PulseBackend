from datetime import datetime

from django.http import JsonResponse
import jwt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from essential.calks.CalculateHours import calculate_total_days

from .models import User, JobTitle, Project, Task
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer
from .basic_comands import db_get


@api_view(['GET', 'POST', 'DELETE'])
def get_all_job_titles(request):

    job_title = JobTitle.objects.all()
    if request.method == 'GET':
        return db_get(job_title, JobTitleSerializer, JobTitle)


def get_all_user_task(request, user_id):
    user_with_task = Task.objects.all().filter(workers=user_id)
    if request.method == 'GET':
        return db_get(user_with_task, TaskSerializer, Task)
def get_all_user_projects(request, user_id):
    user_with_task = Project.objects.all().filter(members=user_id)
    if request.method == 'GET':
        return db_get(user_with_task, ProjectSerializer, Project)

@api_view(['GET'])
def get_all_task_for_project(request,project_id):
    if request.method == 'GET':
        task_for_project = Task.objects.all().filter(project_id=project_id)
        return db_get(task_for_project, TaskSerializer, Task)

def user_worktime_managing(request,user_id):

    all_tasks = Task.objects.all().filter(workers = user_id)

    hoursTotal = calculate_total_days(all_tasks)

    return JsonResponse({'workHours':hoursTotal})

 
        

