
import django
from django.db import models


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
    project_id = models.ForeignKey('Project', on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    daysToAccomplish = models.IntegerField(default=0)
    stageAt = models.CharField(max_length=20,choices=STAGES,default=INTALK)
    priority = models.IntegerField(default=0)
    workers = models.ManyToManyField('User')
    created_at = models.DateField(default=django.utils.timezone.now)

class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    todo  = models.ManyToManyField(Task,blank=True)
    members = models.ManyToManyField('User')
    created_at = models.DateField(default=django.utils.timezone.now)


class User(models.Model):
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    avatar = models.CharField(max_length=800,default="https://www.svgrepo.com/show/192244/man-user.svg")
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    father_name = models.CharField(max_length=800)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=800 , default="работник")


class UserWithTask(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    status = models.CharField(max_length=800)
    work_date = models.DateField(null=True)
    work_time = models.IntegerField(null=True)