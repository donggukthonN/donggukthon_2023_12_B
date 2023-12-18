from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Member

def member_view(request):
    members = Member.objects.all()
    print(members)  # 이 줄을 추가하여 콘솔에 members를 출력합니다.
    return render(request, 'home.html', {"members": members})