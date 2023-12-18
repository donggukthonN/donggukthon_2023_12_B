from django.contrib import auth
from django.views import View
from login.models import Member
from question.models import Question, Answer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date

class Profile(viewsets.ModelViewSet):
  queryset=Member.objects.all()
  @api_view(['GET'])
  def profile(request,u_id):
    member = Member.objects.get(user_id=u_id)
    member_data={
      'user_id' : member.user_id,
      'password' : member.password,
      'nickname' : member.nickname,
      'code' : member.code,
      'startdate' : member.startdate,
    }
    return Response(member_data)