
import datetime
import django
from django.db import models
from rest_framework import generics

class JobTitle(models.Model):
    name = models.CharField(max_length=50)



class Task(models.Model):
    MADE = 'G'
    PROGRESS = 'R'
    INTALK = 'O'
    STAGES = [
(MADE,"Готово"),
(PROGRESS,"В процессе"),
(INTALK,"В обсуждении"),
    ]
#только попробуй вырубить сервер
    project_id = models.ForeignKey('Project', on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    hoursToAccomplish = models.IntegerField(default=0)
    stageAt = models.CharField(max_length=20,choices=STAGES,default=INTALK)
    priority = models.IntegerField(default=0)
    workers = models.ManyToManyField('User')
    created_at = models.DateField(default=datetime.date.today)

class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    members = models.ManyToManyField('User')
    created_at = models.DateField(default=datetime.date.today)

class Issue(models.Model):

    FIXED = 'F'
    NOT_FIXED = 'N'
    STAGES = [
        (FIXED, "исправлено"),
        (NOT_FIXED, "требует исправления")
    ]
    # только попробуй вырубить сервер
    project_id = models.ForeignKey('Project', on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    hoursToAccomplish = models.IntegerField(default=0)
    stageAt = models.CharField(max_length=30, choices=STAGES, default=NOT_FIXED)
    priority = models.IntegerField(default=0)
    workers = models.ManyToManyField('User')
    created_at = models.DateTimeField(default=datetime.date.today)

class User(models.Model):
    WORKER = 'W'
    BOSS = 'B'
    STAGES = [
(WORKER,"Работник"),
(BOSS,"Руководитель"),
    ]
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    avatar = models.CharField(max_length=800,default="https://www.svgrepo.com/show/192244/man-user.svg")
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    father_name = models.CharField(max_length=800)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=80 , choices=STAGES,default=WORKER)

class AllUserTasks(generics.ListAPIView):
    class UserProjectsAndTasks(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        
        def get_user_projects(self, user_id):
            return Project.objects.filter(members=user_id)
        
        def get_user_tasks(self, user_id):
            return Task.objects.filter(workers=user_id)
    
    
