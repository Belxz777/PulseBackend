from rest_framework.decorators import api_view

from .basic_comands import db_get, db_create, db_update, db_delete
from .models import User, JobTitle, Project, Task, Issue
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer


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
        return db_get(project, ProjectSerializer)

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
        return db_get(task, TaskSerializer)

    elif request.method == 'POST':
        return db_create(request, TaskSerializer)

    elif request.method == 'PUT':
        task = Task.objects.get(id=id)
        return db_update(request, TaskSerializer, task)

    elif request.method == 'DELETE':
        return db_delete(Task, id)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def issue_managing(request, id):
    if request.method == 'GET':
        issue = Issue.objects.all().filter(id=id)
        return db_get(issue, IssueSerializer)

    elif request.method == 'POST':
        return db_create(request, IssueSerializer)

    elif request.method == 'PUT':
        issue = Issue.objects.get(id=id)
        return db_update(request, IssueSerializer, issue)

    elif request.method == 'DELETE':
        return db_delete(Issue, id)
