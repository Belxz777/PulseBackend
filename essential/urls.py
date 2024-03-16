from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('users/create',views.RegisterView.as_view()),#для регистрации пользователей
    path("users/login",views.LoginView.as_view()),#дяя входина 
    path("users/auth",views.UserView.as_view()),
    path("users/<id>",views.usersManagingbyId),
    path("get_job_title/",views.getJobTitle),
    path("get_job_title/<id>",views.getJobTitleById),
]