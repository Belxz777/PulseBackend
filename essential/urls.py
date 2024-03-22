from django.urls import path
from . import views, specific_comands

urlpatterns = [
    path("users/login",views.LoginView.as_view()),#дяя входина 
    path("users/auth",views.UserView.as_view()),
    path('users/refresh',views.refresh_token),

    path("user/<id>",views.user_managing),
    path("job_title/<id>",views.job_title_managing),
    path("project/<id>",views.project_managing),
    path("task/<id>",views.task_managing),

    path("all_job_titles", specific_comands.get_all_job_titles),
    path("all_user_task/<user_id>", specific_comands.get_all_user_task),
]