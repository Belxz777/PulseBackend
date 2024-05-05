from django.urls import path

from .utils import specific_comands, token_managing
from . import views
urlpatterns = [
    path('users/create',token_managing.RegisterView.as_view()),#для регистрации пользователей
    path("users/login",token_managing.LoginView.as_view()),#дяя входина
    path("users/auth",token_managing.UserView.as_view()),
    path('users/refresh',token_managing.refresh_token),
    




    path("user/<id>",views.user_managing),
    path("job_title/<id>",views.job_title_managing),
    path("project/<id>",views.project_managing),
    path("task/<id>",views.task_managing),
    path("issue/<id>",views.issue_managing),
    path("department/<id>",views.department_managing),
    path("user_with_task/<id>",views.user_withw_task_managing),


    path("all_job_titles", specific_comands.get_all_job_titles),

    path("task_for_project/<project_id>",specific_comands.get_all_task_for_project),
    path("issue_for_project/<project_id>",specific_comands.get_all_issue_for_project),

    path("all_user_task/<user_id>", specific_comands.get_all_user_task),
    path("all_user_issue/<user_id>", specific_comands.get_all_user_issue),
    path("all_user_projects/<user_id>", specific_comands.get_all_user_projects),

    path('user_worktime/<user_id>',specific_comands.user_worktime_managing),
    path('userbyName/<user_name>',specific_comands.getUserByName),

    path('get_all_departments',specific_comands.get_all_departments),
    path('get_all_department_members/<department_id>',specific_comands.get_all_department_members),

    path('get_all_UserWithTask_for_user/<user_id>',specific_comands.get_all_UserWithTask_for_user),
    path('get_all_UserWithTask_for_task/<task_id>',specific_comands.get_all_UserWithTask_for_task),
    path('get_all_UserWithTask_for_issue/<issue_id>',specific_comands.get_all_UserWithTask_for_issue),
    path('get_all_UserWithTask_for_project/<project_id>',specific_comands.get_all_UserWithTask_for_project)
]