from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
from .basic_comands import db_get

@api_view(['GET'])
def department_report(request,department_id):

    users = User.objects.all().filter(department_id=department_id)
