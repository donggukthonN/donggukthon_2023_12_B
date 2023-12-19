from django.contrib import auth
from django.views import View
from login.models import Member
from question.models import Question, Answer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class Profile(viewsets.ModelViewSet):
  queryset=Member.objects.all()
  @api_view(['GET'])
  def profile(request,u_id):
    member = Member.objects.get(userId=u_id)
    member_data={
      'userId' : member.userId,
      'password' : member.password,
      'nickname' : member.nickname,
      'code' : member.code,
      'startDate' : member.startDate,
    }
    return Response(member_data)
  

class Book(viewsets.ModelViewSet):
  queryset=Member.objects.all()
  @api_view(['GET'])
  def book(request,u_id):
    questions = []
    answer = Answer.objects.filter(user__userId=u_id) # 대답은 u_id에 맞는 사람의 대답을 들고와야 함
    userId = Member.objects.get(userId=u_id).userId
    for i in range(1,26): # 질문의 num은 1부터 25까지
      question = Question.objects.get(num=i)
      answer_filter = answer.filter(num=i)
      
      if not answer_filter.exists(): # answer_instances가 비어있는 경우에 대한 처리
          content = None
          flag = None
      else:
          content = answer_filter.first().content
          flag = answer_filter.first().flag
          
      book_data={
        'questionNum' : i,
        'question' : question.content,
        'answer' : content,
        'flag' : flag
      }
      questions.append(book_data)
    
    return Response({'userId':userId, 'questions' : questions})
  
# class Friend(viewsets.ModelViewSet):
#   queryset=Friend.objects.all()
#   @api_view(['GET'])
#   def friend(request,u_id):
#     userId = Member.objects.get(userId=u_id).userId
#     # ~~