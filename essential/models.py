from django.db import models

# Create your models here.
from datetime import datetime, timedelta
from django.db import models

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

class JobTitle(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)


class Task(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)


class User(models.Model):
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    father_name = models.CharField(max_length=800)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class WorkOnTask(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT)
    work_date = models.DateField()
    work_time = models.IntegerField(default=0)


class UserWithTask:
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT)
    status = models.CharField(max_length=800)

    
    