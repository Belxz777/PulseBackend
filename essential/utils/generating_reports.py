from datetime import datetime
from io import BytesIO
from django.http import FileResponse, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer
from pdfdocument.document import PDFDocument

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter, A4



@api_view(['GET'])
def department_report(request,department_id):
    if request.method == 'GET':


        user_with_task = dict()
        users = User.objects.all().filter(department_id=department_id)
        
        for i in users:
            user_with_task[str(i.id)] = list(UserWIthTask.objects.filter(user_id = i.id).values())
        
        # result = json.dumps(user_with_task, indent = 10, default=str)
        # res = say_hello(user_with_task)
        # return HttpResponse(res, charset = "UTF-16", content_type = "application/pdf")

        return HttpResponse(hello(user_with_task,department_id), content_type='application/pdf')

# def say_hello(data=None):   
#     f = BytesIO()
#     pdf = PDFDocument(f)
#     pdf.init_report()

#     pdfmetrics.registerFont(TTFont('DejaVuSerif','DejaVuSerif.ttf', 'UTF-8'))

#     for i in data:
#         pdf.generate_style('DejaVuSerif',20)
#         user = User.objects.get(id = int(i))
#         pdf.h1(user.last_name + " " + user.first_name + " " + user.father_name)

#         pdf.generate_style('DejaVuSerif',20)
        
#         for j in data[i]:
#             a = j.keys()
#             for k in a:
                
#                 pdf.p('      ' + k + ':'+ str(j[k]))
#                 pdf.spacer(10.0)

#     pdf.generate()
#     return f.getvalue()


def hello(data=None,department_id = 0):

    w,h = A4

    name_x = 20
    work_x = 50
    start_y = h-50
    delta_y_for_name = 30
    delta_y_for_work = 20

    pdfmetrics.registerFont(TTFont('DejaVuSerif','DejaVuSerif.ttf', 'UTF-8'))
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = 'filename="file.pdf"'
   
    c = canvas.Canvas(response,pagesize=A4)  

    for i in data:
            
            print(i)
            
            user = User.objects.get(id = int(i))
            c.setFont("DejaVuSerif",20)
            c.drawString(name_x,start_y, user.last_name + " " + user.first_name + " " + user.father_name)
            start_y = start_y - delta_y_for_name

            for j in data[i]:

                print(j)

                c.setFont("DejaVuSerif",10)
                if j["work_type"] == "T":
                    work = Task.objects.get(id = int(j["work_id_id"]))
                    c.drawString(work_x,start_y, j["created_at"].strftime("%m/%d/%Y") + ': пороботал над задачей "' + work.name + '" в течение ' + str(j["work_time"]) + " часов")
                    start_y = start_y - delta_y_for_work

                elif j["work_type"] == "I":
                    work = Issue.objects.get(id = int(j["work_id_id"]))
                    c.drawString(work_x,start_y, j["created_at"].strftime("%m/%d/%Y") + ': поиспровлял ошибку "' + work.name + '" в течение ' + str(j["work_time"]) + " часов")
                    start_y = start_y - delta_y_for_work

            start_y = start_y - delta_y_for_name
    d = Department.objects.get(id = department_id)
    c.setTitle('Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    c.showPage()
    c.save()

    return response