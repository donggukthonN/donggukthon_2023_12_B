from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from login import views as login_views
from question import views as question_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_views.member_view,name="home"),
    path('login/',login_views.Login.login,name='login'),
    path('signup/duplicate/',login_views.SignUp.check_duplicate_user,name='duflicate'),
    path('signup/',login_views.SignUp.signup,name='signup'),
    path('<str:u_id>/question/<int:q_id>/',question_views.ShowQuestion.show_question,name="show_question"),
]
