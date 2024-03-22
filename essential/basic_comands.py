from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project, Task, UserWithTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, UserWithTaskSerializer


def db_get(objects=[], Serializer=UsersSerializer(), curent_class=User()):
    send_data = []

    try:
        for i in objects:
            serializer = Serializer(i)
            send_data.append(serializer.data)
        if len(send_data) == 1:
            return JsonResponse(send_data[0], safe=False)
        return JsonResponse(send_data, safe=False)

    except curent_class.DoesNotExist:
        return JsonResponse({'message': 'The job_title does not exist'}, status=404)


def db_create(request, Serializer=None):
    data = JSONParser().parse(request)
    serializer = Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


def db_update(request, Serializer=None, instanse=None):
    data = JSONParser().parse(request)
    serializer = Serializer(instanse, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)
