from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.views import View
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

