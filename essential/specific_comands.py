from datetime import datetime

from django.http import JsonResponse
from rest_framework.decorators import api_view

from essential.utils.CalculateHours import calculate_total_days

from .models import User, JobTitle, Project, Task, Issue
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer
from .basic_comands import db_get

# про job_title
@api_view(['GET'])
def get_all_job_titles(request):
    if request.method == 'GET':
        job_title = JobTitle.objects.all()
        return db_get(job_title, JobTitleSerializer, JobTitle)



# про user
@api_view(['GET'])
def get_all_user_task(request, user_id):
    if request.method == 'GET':
        user_with_task = Task.objects.all().filter(workers=user_id)
        return db_get(user_with_task, TaskSerializer, Task)


def get_all_user_issue(request, user_id):
    if request.method == 'GET':
        user_with_issue = Issue.objects.all().filter(workers=user_id)
        return db_get(user_with_issue, IssueSerializer, Issue)

@api_view(['GET'])
def user_worktime_managing(request, user_id):
    if request.method == 'GET':
        all_tasks = Task.objects.all().filter(workers=user_id)
        hoursTotal = calculate_total_days(all_tasks)
        return JsonResponse({'workHours': hoursTotal})

@api_view(['GET'])
def getUserByName(request, user_name):
    if request.method == 'GET':
        user = User.objects.all().filter(last_name__startswith=user_name)
        return db_get(user, UsersSerializer, User)




# про project
@api_view(['GET'])
def get_all_user_projects(request, user_id):
    if request.method == 'GET':
        user_with_task = Project.objects.all().filter(members=user_id)
        return db_get(user_with_task, ProjectSerializer, Project)


@api_view(['GET'])
def get_all_task_for_project(request, project_id):
    if request.method == 'GET':
        task_for_project = Task.objects.all().filter(project_id=project_id)
        return db_get(task_for_project, TaskSerializer, Task)

def get_all_issue_for_project(request, project_id):
    if request.method == 'GET':
        issue_for_project = Issue.objects.all().filter(project_id=project_id)
        return db_get(issue_for_project, IssueSerializer, Issue)
