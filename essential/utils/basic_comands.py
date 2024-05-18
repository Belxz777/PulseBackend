from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# взаимодействие с базой данных:

# получение

# добавление

# обновление

# удаление

def db_get(objects=[], Serializer=None, curent_class=None):
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
    print(request)
    data = JSONParser().parse(request)
    serializer = Serializer(data=data)  
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


def db_update(request, Serializer=None, instanse=None):
    serializer = Serializer(instanse, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


def db_delete(curent_class = None, id = 0):
    response = Response()
    try:
        object = curent_class.objects.get(id=id)
        object.delete()
        response.data = {"massage":"object deleted successfully"}
    except:
        response.data = {"massage":"error: object was not deleted"}
    return response