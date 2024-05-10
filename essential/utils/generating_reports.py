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
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4



@api_view(['GET'])
def department_report(request,department_id):
    if request.method == 'GET':

        user_with_task = dict()
        users = User.objects.all().filter(department_id=department_id)
        
        for i in users:
            user_with_task[str(i.id)] = list(UserWIthTask.objects.filter(user_id = i.id).values())

        return HttpResponse(hello(user_with_task,department_id), content_type='application/pdf')


def hello(data=None,department_id = 0):

    w,h = A4

    name_x = 20
    work_x = 50
    start_y = h-h/20
    delta_y_for_name = 30
    delta_y_for_work = 20


    styles = getSampleStyleSheet()
    styles['Normal'].fontName='DejaVuSerif'
    styles['Heading1'].fontName='DejaVuSerif'
    pdfmetrics.registerFont(TTFont('DejaVuSerif','DejaVuSerif.ttf', 'UTF-8'))
    
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = 'filename="file.pdf"'
   
    c = canvas.Canvas(response,pagesize=A4)  

    d = Department.objects.get(id = department_id)
    c.setTitle('Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

    c.setFont("DejaVuSerif",15)
    title_w = c.stringWidth('Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"DejaVuSerif",15)
    c.drawString(w/2-title_w/2,start_y, 'Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    start_y = start_y - delta_y_for_name*2

    for i in data:
            
            user = User.objects.get(id = int(i))
            c.setFont("DejaVuSerif",20)
            c.drawString(name_x,start_y, user.last_name + " " + user.first_name + " " + user.father_name)
            start_y = start_y - delta_y_for_name

            
            for j in data[i]:

                c.setFont("DejaVuSerif",10)
                

                if j["work_type"] == "T":
                    work = Task.objects.get(id = int(j["work_id_id"]))
                    p = Project.objects.get(id = work.project_id_id)
                    c.drawString(work_x,start_y, j["created_at"].strftime("%d/%m/%Y") + ' - "' + p.name + '" : задача "' + work.name + '" - ' + str(j["work_time"]) + " часов")
                    start_y = start_y - delta_y_for_work

                elif j["work_type"] == "I":
                    work = Issue.objects.get(id = int(j["work_id_id"]))
                    p = Project.objects.get(id = work.project_id_id)
                    c.drawString(work_x,start_y, j["created_at"].strftime("%d/%m/%Y") + ' - "' + p.name + '" : ошибка "' + work.name + '" - ' + str(j["work_time"]) + " часов")
                    start_y = start_y - delta_y_for_work
            
                if start_y < h/20:
                    c.showPage()
                    start_y = h-h/20

            start_y = start_y - delta_y_for_work

    
    c.showPage()
    c.save()

    return response