from datetime import datetime
import io
import xlsxwriter
from django.http import FileResponse, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from ..models import User, JobTitle, Project, Task, Issue, Department, UserWIthTask
from ..serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, IssueSerializer, DepartmentSerializer, UserWithTaskSerializer

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4

import random

@api_view(['GET'])
def department_report(request,department_id):
    if request.method == 'GET':

        user_with_task = dict()
        users = User.objects.all().filter(department_id=department_id)
        
        for i in users:
            user_with_task[str(i.id)] = list(UserWIthTask.objects.filter(user_id = i.id).values())
        print(user_with_task)

        return export_page(user_with_task,department_id)


def export_page(data=None,department_id = 0):

    _x_name = 0
    _x_work = 0
    _y_name = 0
    _y_work = 0
    _y_colomns = 0

    name_colomns = ["Фамилия","Имя","Отчество","Должность","Статус","Время работы"]
    work_colomns = ["Сотрудник","Дата","Проект","Тип работы","Задача|Исправление"," Время работы","Резерв","ЗНО","ЗНИ =20","ЗНИ >20","Постоянные\n и адм. работы\n (поручения,\n встречи,\n обучение и тд.)",
                    "Регламентные работы","Техдолг","Отсутствия\n (больничные,\n отпуска,\n отгулы)","Комментарий"]
    default_values = [[" "],[41.00,129.00,16.00],[18.00,8.00,16.00],[20.00,71.00],[42.00,6.00,7,00,24.00],["да","нет","нет","нет"],[12.00,14.00,16.00],["больничный","отпуск","отгул","","","","",""]]

    d = Department.objects.get(id = department_id)

    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet_names = workbook.add_worksheet("сотрудники")
    worksheet_works = workbook.add_worksheet("выполненная работа")

    bold = workbook.add_format({'bold': True})

    for i in name_colomns:
        worksheet_names.write(_x_name,_y_colomns,i,bold)
        _y_colomns += 1
    _y_colomns = 0
    for i in work_colomns:
        worksheet_works.write(_x_work,_y_colomns,i,bold)
        _y_colomns += 1
    _x_name = _x_name + 1
    _x_work = _x_work + 1

    for i in data:
            
        user = list(User.objects.filter(id = int(i)).values())
        user = user[0]
        total_user_hours = 0
    
        for j in data[i]:
            _y_work = 0
            if j["work_type"] == "T":

                work = Task.objects.get(id = int(j["work_id"]))
                p = Project.objects.get(id = work.project_id_id)

                worksheet_works.write(_x_work, _y_work,  user["last_name"]+" "+user["first_name"]+" "+user["father_name"])
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, j["created_at"].strftime("%d/%m/%Y"))
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, p.name)
                _y_work += 1
                worksheet_works.write(_x_work, _y_work,"задача")
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, work.name)
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, str(j["work_time"]))
                _y_work += 1

                for def_val in default_values:
                    if len(def_val) == 1:
                        worksheet_works.write(_x_work, _y_work,  def_val[0])
                        print(def_val)
                        _y_work += 1
                    else:
                        r_v = random.randint(0,len(def_val)-1)
                        print(r_v,def_val)
                        worksheet_works.write(_x_work, _y_work,  def_val[r_v])
                        _y_work += 1

                total_user_hours += j["work_time"]

            if j["work_type"] == "I":
                
                work = Issue.objects.get(id = int(j["work_id"]))
                p = Project.objects.get(id = work.project_id_id)

                worksheet_works.write(_x_work, _y_work,  user["last_name"]+" "+user["first_name"]+" "+user["father_name"])
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, j["created_at"].strftime("%d/%m/%Y"))
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, p.name)
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, "ошибка")
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, work.name)
                _y_work += 1
                worksheet_works.write(_x_work, _y_work, str(j["work_time"]))
                _y_work += 1

                worksheet_works.write(_x_work, _y_work, str(j["work_time"]))
                for def_val in default_values:
                    if len(def_val) == 1:
                        worksheet_works.write(_x_work, _y_work,  def_val[0])
                        print(def_val)
                        _y_work += 1
                    else:
                        r_v = random.randint(0,len(def_val)-1)
                        print(r_v,def_val)
                        worksheet_works.write(_x_work, _y_work,  def_val[r_v])
                        _y_work += 1

                total_user_hours += j["work_time"]

            _x_work = _x_work + 1

        worksheet_names.write(_x_name,_y_name, user["last_name"])
        _y_name += 1
        worksheet_names.write(_x_name,_y_name,user["first_name"])
        _y_name += 1
        worksheet_names.write(_x_name,_y_name,user["father_name"])
        _y_name += 1
        worksheet_names.write(_x_name,_y_name,JobTitle.objects.get(id = int(user["job_title_id_id"])).name)
        _y_name += 1
        worksheet_names.write(_x_name,_y_name, user["position"])
        _y_name += 1
        worksheet_names.write(_x_name,_y_name, total_user_hours)
        _y_name += 1

        _x_name = _x_name + 1
        _y_name = 0
                    
    worksheet_works.autofit()
    worksheet_names.autofit()
    workbook.close()
    buffer.seek(0)
    f_name = d.name + "-" + datetime.now().strftime("%d.%m.%Y")+".xlsx"
    print(f_name)

    return FileResponse(buffer, as_attachment=False, filename = f_name)





# def hello(data=None,department_id = 0):

#     w,h = A4

#     name_x = 20
#     work_x = 50
#     start_y = h-h/20
#     delta_y_for_name = 30
#     delta_y_for_work = 20

#     # "MIROSLN", "FreeSans"
#     current_font = "FreeSans"

#     pdfmetrics.registerFont(TTFont(current_font,current_font+"/"+current_font+".ttf"))
    
#     response = HttpResponse(content_type='application/pdf') 
#     response['Content-Disposition'] = 'filename="file.pdf"'
   
#     c = canvas.Canvas(response,pagesize=A4)  

#     d = Department.objects.get(id = department_id)
#     c.setTitle('Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

#     c.setFont(current_font,15)
#     title_w = c.stringWidth('Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),current_font,15)
#     c.drawString(w/2-title_w/2,start_y, 'Отчёт по отделу "' + d.name + '" за ' + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
#     start_y = start_y - delta_y_for_name*2

#     for i in data:
            
#             user = User.objects.get(id = int(i))
#             c.setFont(current_font,20)
#             c.drawString(name_x,start_y, user.last_name + " " + user.first_name + " " + user.father_name)
#             start_y = start_y - delta_y_for_name

            
#             for j in data[i]:

#                 c.setFont(current_font,10)
                

#                 if j["work_type"] == "T":
#                     work = Task.objects.get(id = int(j["work_id_id"]))
#                     p = Project.objects.get(id = work.project_id_id)
#                     c.drawString(work_x,start_y, j["created_at"].strftime("%d/%m/%Y") + ' - "' + p.name + '" : задача "' + work.name + '" - ' + str(j["work_time"]) + " часов")
#                     start_y = start_y - delta_y_for_work

#                 elif j["work_type"] == "I":
#                     work = Issue.objects.get(id = int(j["work_id_id"]))
#                     p = Project.objects.get(id = work.project_id_id)
#                     c.drawString(work_x,start_y, j["created_at"].strftime("%d/%m/%Y") + ' - "' + p.name + '" : ошибка "' + work.name + '" - ' + str(j["work_time"]) + " часов")
#                     start_y = start_y - delta_y_for_work
            
#                 if start_y < h/20:
#                     c.showPage()
#                     start_y = h-h/20

#             start_y = start_y - delta_y_for_work

    
#     c.showPage()
#     c.save()

#     return response