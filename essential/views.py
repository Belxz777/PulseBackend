from django.http import JsonResponse
from rest_framework.decorators import api_view

from .utils.basic_comands import db_get, db_create, db_update, db_delete
from .models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
from django.core.cache import cache
import datetime

def delete_expired_tasks():
    expired_tasks = Task.objects.filter(stageAt="готово", created_at=datetime.date.today()-datetime.timedelta(days=2))
    expired_tasks.delete()
    print('Deleted',expired_tasks.count())


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def user_managing(request, id):
    if request.method == 'GET':
    #    userDataChache = cache.get('userData')
    #    if userDataChache is None:
    #     userDataChache = User.objects.all().filter(id=id)
    #     cache.set('userData', userDataChache, 10)
    #    else:
    #     total = userDataChache
    #     print(userDataChache)

        


        user = User.objects.all().filter(id=id)
        return db_get(user, UsersSerializer, User)

    elif request.method == 'POST':
        return db_create(request, UsersSerializer)

    elif request.method == 'PATCH':
        user = User.objects.get(id=id)
        return db_update(request, UsersSerializer, user)


    elif request.method == 'DELETE':
        return db_delete(User, id)


@api_view(['GET', 'POST', 'DELETE', "PATCH"])
def job_title_managing(request, id):
    if request.method == 'GET':
        job = JobTitle.objects.all().filter(id=id)
        return db_get(job, JobTitleSerializer, JobTitle)

    elif request.method == 'POST':
        return db_create(request, JobTitleSerializer)

    elif request.method == 'PATCH':
        job = JobTitle.objects.get(id=id)
        return db_update(request, JobTitleSerializer, job)

    elif request.method == 'DELETE':
        return db_delete(JobTitle, id)


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def project_managing(request, id):
    if request.method == 'GET':
        project = Project.objects.all().filter(id=id)
        return db_get(project, ProjectSerializer)

    elif request.method == 'POST':
        return db_create(request, ProjectSerializer)

    elif request.method == 'PATCH':
        project = Project.objects.get(id=id)
        return db_update(request, ProjectSerializer, project)

    elif request.method == 'DELETE':
        return db_delete(Project, id)


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def task_managing(request, id):
    if request.method == 'GET':
        task = Task.objects.all().filter(id=id)
        return db_get(task, TaskSerializer)

    elif request.method == 'POST':
        return db_create(request, TaskSerializer)

    elif request.method == 'PATCH':
        task = Task.objects.get(id=id)
        return db_update(request, TaskSerializer, task)

    elif request.method == 'DELETE':
        return db_delete(Task, id)


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def issue_managing(request, id):
    if request.method == 'GET':
        issue = Issue.objects.all().filter(id=id)
        return db_get(issue, IssueSerializer, Issue)

    elif request.method == 'POST':
        return db_create(request, IssueSerializer)

    elif request.method == 'PATCH':
        issue = Issue.objects.get(id=id)
        return db_update(request, IssueSerializer, issue)

    elif request.method == 'DELETE':
        return db_delete(Issue, id)
    

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def department_managing(request, id):
    if request.method == 'GET':
        department = Department.objects.all().filter(id=id)
        return db_get(department, DepartmentSerializer)

    elif request.method == 'POST':
        return db_create(request, DepartmentSerializer)

    elif request.method == 'PATCH':
        department = Department.objects.get(id=id)
        return db_update(request, DepartmentSerializer, department)

    elif request.method == 'DELETE':
        return db_delete(Department, id)


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def user_withw_task_managing(request, id):
    if request.method == 'GET':
        user_with_task = UserWIthTask.objects.all().filter(id=id)
        return db_get(user_with_task, UserWithTaskSerializer)
    
    elif request.method == 'POST':
        return db_create(request, UserWithTaskSerializer)
    
    elif request.method == 'PATCH':
        user_with_task = UserWIthTask.objects.get(id=id)
        return db_update(request, UserWithTaskSerializer, user_with_task)
    
    elif request.method == 'DELETE':
        return db_delete(UserWIthTask, id)
