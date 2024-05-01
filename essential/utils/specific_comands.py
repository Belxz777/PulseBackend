from datetime import datetime

from django.http import JsonResponse
from rest_framework.decorators import api_view

from essential.utils.CalculateHours import calculate_total_days

from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
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

@api_view(['GET'])
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

@api_view(['GET'])
def get_all_issue_for_project(request, project_id):
    if request.method == 'GET':
        issue_for_project = Issue.objects.all().filter(project_id=project_id)
        return db_get(issue_for_project, IssueSerializer, Issue)




# про departments

@api_view(['GET'])
def get_all_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        return db_get(departments, DepartmentSerializer, Department)

@api_view(['GET'])
def get_all_department_members(request, department_id):
    if request.method == 'GET':
            members = User.objects.all().filter(department_id=department_id)
            return db_get(members, UsersSerializer, User)




# про user_with_task
WORK_TYPES = {"task":Task,"issue":Issue}

@api_view(['GET'])
def get_all_UserWithTask_for_user(request, user_id):
    if request.method == 'GET':
        user_with_task = UserWIthTask.objects.all().filter(user_id=user_id)
        return db_get(user_with_task, UserWithTaskSerializer, UserWIthTask)
    
@api_view(['GET'])
def get_all_UserWithTask_for_task(request, task_id):
    if request.method == 'GET':
        user_with_task = UserWIthTask.objects.all().filter(work_id=task_id, work_type = "T")
        return db_get(user_with_task, UserWithTaskSerializer, UserWIthTask)
    
@api_view(['GET'])
def get_all_UserWithTask_for_issue(request, issue_id):
    if request.method == 'GET':
        user_with_task = UserWIthTask.objects.all().filter(work_id=issue_id, work_type = "I")
        return db_get(user_with_task, UserWithTaskSerializer, UserWIthTask)
    
@api_view(['GET'])    
def get_all_UserWithTask_for_project(request, project_id):
    if request.method == 'GET':
        Tid = [i.id for i in Task.objects.all().filter(project_id =project_id)]
        Iid = [i.id for i in Issue.objects.all().filter(project_id =project_id)]

        res = []

        for i in Tid:
            user_with_task = UserWIthTask.objects.all().filter(work_id = i, work_type = "T")
            for j in user_with_task:
                res.append(j)
        for i in Iid:
            user_with_task = UserWIthTask.objects.all().filter(work_id = i, work_type = "I")
            for j in user_with_task:
                res.append(j)

        return db_get(res, UserWithTaskSerializer, UserWIthTask)