from django.http import JsonResponse
from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer

@api_view(['GET'])
def delete_if_finished(request, work_name):
    if request.method == 'GET':
        t = 0
        u = 0
        if work_name == 'task':
            tasks = Task.objects.all().filter(stageAt='Готово')
            for i in tasks:
                user_with_task = UserWIthTask.objects.all().filter(work_id=i.id, work_type='T')
                for j in user_with_task:
                    u += 1
                    j.delete()
                t += 1
                i.delete()
        elif work_name == 'issue':
            tasks = Issue.objects.all().filter(stutus='Закрыто')
            for i in tasks:
                user_with_task = UserWIthTask.objects.all().filter(work_id=i.id, work_type='I')
                for j in user_with_task:
                    u += 1
                    j.delete()
                t += 1
                i.delete()
        return JsonResponse({'message': str(t) +' tasks deleted, '+ str(u) +' user_with_task deleted'})
