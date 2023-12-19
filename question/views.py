from django.shortcuts import get_object_or_404
from django.views import View
from login.models import Member
from question.models import Question, Answer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ShowQuestion(viewsets.ModelViewSet):
      @api_view(['GET'])
      def show_question(request,u_id,q_id):
            question = Question.objects.get(num=q_id)
            question_data = {
                  'questionNum': question.num,
                  'content': question.get_content_with_newlines(),
            }
            return Response(question_data)

class PostAnswer(viewsets.ModelViewSet):
      @api_view(['POST'])
      def post_answer(request, u_id, q_id):
            user = get_object_or_404(Member, userId=u_id)
            num = get_object_or_404(Question, num=q_id)
            content = request.data.get('content')
            flag = request.data.get('flag')

            # Answer 모델에 데이터 저장
            Answer.objects.create(user=user, num=num, content=content, flag=flag)