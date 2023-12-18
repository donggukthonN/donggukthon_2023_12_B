from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth import logout
from django.views import View
from login.models import Member
from question.models import Question, Answer
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date

class ShowQuestion(viewsets.ModelViewSet):
    @api_view(['GET'])
    def show_question(request,u_id,q_id):
      question = Question.objects.get(num=q_id)
      question_data = {
            'num': question.num,
            'content': question.content,
      }
      return Response({'question': question_data})

class PostAnswer(viewsets.ModelViewSet):
    @api_view(['POST'])
    def post_answer(request, u_id, q_id):
      user_instance = get_object_or_404(Member, user_id=u_id)
      question_instance = get_object_or_404(Question, num=q_id)
      content = request.data.get('content')
      flag = request.data.get('flag')

      # Answer 모델에 데이터 저장
      Answer.objects.create(user=user_instance.user_id, num=question_instance.num, content=content, flag=flag)
      
      return Response({'message': 'Answer posted successfully'})