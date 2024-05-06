from io import BytesIO
import json
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
from io import BytesIO
from pdfdocument.document import PDFDocument


@api_view(['GET'])
def department_report(request,department_id):
    if request.method == 'GET':


        user_with_task = dict()
        users = User.objects.all().filter(department_id=department_id)
        
        for i in users:
            user_with_task[str(i.id)] = list(UserWIthTask.objects.filter(user_id = i.id).values())
        
        result = json.dumps(user_with_task, indent = 10, default=str)
        print(result)

        # pdf, response = pdf_response(result)
        # pdf.generate()
        res = say_hello(user_with_task)
        print(type(res))

        return HttpResponse(res, content_type='application/pdf')


def say_hello(data=None):   
    f = BytesIO()
    pdf = PDFDocument(f)
    pdf.init_report()

    for i in data:
        pdf.h3(i)
        for j in data[i]:
            a = j.keys()
            for k in a:
                pdf.p(k + ':'+ str(j[k]))
    # pdf.h1('Hello World')
    # pdf.p('Creating PDFs made easy.')

    pdf.generate()
    return f.getvalue()