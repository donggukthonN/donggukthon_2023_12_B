from django.shortcuts import get_object_or_404
from django.views import View
from login.models import Member
from question.models import Question, Answer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

class ShowQuestion(viewsets.ModelViewSet):
      @api_view(['GET'])
      def show_question(request,u_id,q_id):
            question = Question.objects.get(num=q_id)
            question_data = {
                  'questionNum': question.num,
                  'content': question.get_content_with_newlines(),
            }
            print(question_data)
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
            return Response({'success':True})
            
class GetCalendar(viewsets.ModelViewSet):
      queryset=Member.objects.all()
      @api_view(['GET'])
      def get_calendar(request,u_id,q_id):
            question = Question.objects.get(num=q_id) # 질문 불러오기
            answer = Answer.objects.filter(user__userId=u_id) # 대답은 u_id에 맞는 사람의 대답을 들고와야 함
            answer_filter = answer.filter(num=q_id) # 답 불러오기
            answer_content = answer_filter.first().content
            
            return Response({"question":question.content,"answer":answer_content})
      
class PutCalendar(viewsets.ModelViewSet):
      queryset = Member.objects.all()

      @api_view(['PUT'])
      @transaction.atomic
      def put_calendar(request, u_id, q_id):
            # 기존의 answer 삭제
            Answer.objects.filter(user_id=u_id, num=q_id).delete()

            # 새로운 값 추가
            new_answer = request.data.get('content')
            new_flag = request.data.get('flag')

            Answer.objects.create(user_id=u_id, num_id=q_id, content=new_answer, flag=new_flag)

            return Response({'success': True, 'message': 'Calendar updated successfully'})