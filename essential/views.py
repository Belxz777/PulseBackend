from rest_framework.decorators import api_view

from .basic_comands import db_get, db_create, db_update, db_delete
from .models import User, JobTitle, Project, Task
from .serializer import  UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_managing(request, id):
    if request.method == 'GET':
        user = User.objects.all().filter(id=id)
        return db_get(user, UsersSerializer, User)

    elif request.method == 'POST':
        return db_create(request, UsersSerializer)

    elif request.method == 'PUT':
        user = User.objects.get(id=id)
        return db_update(request, UsersSerializer, user)
        
    elif request.method == 'DELETE':
        return db_delete(User, id)


@api_view(['GET', 'POST', 'DELETE', "PUT"])
def job_title_managing(request, id):
    if request.method == 'GET':
        job = JobTitle.objects.all().filter(id=id)
        return db_get(job, JobTitleSerializer, JobTitle)

    elif request.method == 'POST':
        return db_create(request, JobTitleSerializer)

    elif request.method == 'PUT':
        job = JobTitle.objects.get(id=id)
        return db_update(request, JobTitleSerializer, job)

    elif request.method == 'DELETE':
        return db_delete(JobTitle, id)



@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def project_managing(request, id):


    if request.method == 'GET':
        project = Project.objects.all().filter(id=id)
        return db_get(project,ProjectSerializer)

    elif request.method == 'POST':
        return db_create(request, ProjectSerializer)

    elif request.method == 'PUT':
        project = Project.objects.get(id=id) 
        return db_update(request, ProjectSerializer, project)

    elif request.method == 'DELETE':
        return db_delete(Project, id)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def task_managing(request, id):


    if request.method == 'GET':
        task = Task.objects.all().filter(id=id)
        return db_get(task,TaskSerializer)

    elif request.method == 'POST':
        return db_create(request, TaskSerializer)

    elif request.method == 'PUT':
        task = Task.objects.get(id=id)
        return db_update(request, TaskSerializer, task)

    elif request.method == 'DELETE':
        return db_delete(Task, id)

def getAllUserProjects(request,user_id):
        projects = Project.objects.all().filter(members=user_id)
        return db_get(projects,ProjectSerializer)


















""" @api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_with_task_managing(request, id):
    user_with_task = UserWithTask.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)

    elif request.method == 'POST':
        return db_create(request, UserWithTaskSerializer)

    elif request.method == 'PUT':
        uwt = UserWithTask.objects.get(id=id)
        return db_update(request, UserWithTaskSerializer, uwt)
    
    elif request.method == 'DELETE':
        return db_delete(UserWithTask, id) """