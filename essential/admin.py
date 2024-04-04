from django.contrib import admin

from essential.models import Project,User,Task,JobTitle

# Register your models here.
admin.site.register(Project)
admin.sitesite_header = 'Админка'
admin.site.register(Task)
admin.site.register(User)
admin.site.register(JobTitle)

