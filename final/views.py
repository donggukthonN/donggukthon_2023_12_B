from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.views import View
from login.models import Member
from question.models import Question, Answer
from final.models import Friend
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

class UserBook(viewsets.ModelViewSet):
    queryset=Member.objects.all()
    @api_view(['GET'])
    def user_book(request,u_id):
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

class GetFriend(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    @api_view(['GET'])
    def get_friend(request, u_id):
        # 특정 u_id와 일치하는 Member 객체 가져오기
        user_member = get_object_or_404(Member, userId=u_id)

        # 특정 user와 관련된 Friend 레코드 가져오기
        friends = Friend.objects.filter(user=user_member)

        # friends 데이터 구성
        friends_data = [{'id': f.f_id} for f in friends]

        # Answer 모델의 content 필드 중 하나라도 null 값이 있는지 확인
        for friend_data in friends_data:
            friend_member = Member.objects.get(userId=friend_data['id'])
            answer_count = Answer.objects.filter(user=friend_member).exclude(content=None).count()

            # Answer 25개가 전부 채워져 있다면 'complete' : 1을 추가, 그렇지 않으면 'complete' : 0을 추가
            friend_data['complete'] = 1 if answer_count == 25 else 0

        return Response({'friends': friends_data})


class AddFriend(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    @api_view(['POST'])
    def add_friend(request, u_id):
        f_id = request.data.get('f_id')
        code = request.data.get('code')

        current_user = get_object_or_404(Member, userId=u_id)

        try:
            friend_member = Member.objects.get(userId=f_id, code=code)
        except Member.DoesNotExist:
            return Response({'success': False, 'message': 'Invalid f_id or code'})

        # 이미 친구 관계가 있는지 확인
        if Friend.objects.filter(user=current_user, f_id=f_id).exists():
            return Response({'success': False, 'message': 'Friendship already exists'})

        # 친구 추가
        friend = Friend.objects.create(user=current_user, f_id=f_id)
        friend.save()

        # 상대편도 친구 추가
        reverse_friend = Friend.objects.create(user=friend_member, f_id=u_id)
        reverse_friend.save()

        return Response({'success': True, 'message': 'Friend added successfully'})

class DeleteFriend(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    @api_view(['DELETE'])
    def delete_friend(request, u_id, f_id):
        # 현재 사용자의 Member 객체 가져오기
        current_user = get_object_or_404(Member, userId=u_id)

        try:
            # 친구의 Member 객체 가져오기
            friend_member = Member.objects.get(userId=f_id)
        except Member.DoesNotExist:
            return Response({'success': False, 'message': 'Invalid f_id'})

        # Friend 모델에서 친구 삭제
        friend1 = get_object_or_404(Friend, user=current_user, f_id=f_id)
        friend2 = get_object_or_404(Friend, user=friend_member, f_id=u_id)

        # 양방향 삭제
        friend1.delete()
        friend2.delete()

        return Response({'success': True, 'message': 'Friend deleted successfully'})

class FriendBook(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    @api_view(['GET'])
    def friend_book(request, u_id, f_id):
        # 현재 사용자의 Member 객체 가져오기
        current_user = get_object_or_404(Member, userId=u_id)

        try:
            # 친구의 Member 객체 가져오기
            friend_member = Member.objects.get(userId=f_id)
        except Member.DoesNotExist:
            return Response({'success': False, 'message': 'Invalid f_id'})

        # 친구의 대답 가져오기
        friend_answer = Answer.objects.filter(user__userId=f_id)

        questions = []
        for i in range(1, 26):  # 질문의 num은 1부터 25까지
            question = Question.objects.get(num=i)
            answer_filter = friend_answer.filter(num=i)

            if not answer_filter.exists():  # answer_instances가 비어있는 경우에 대한 처리
                content = None
                flag = None
            else:
                content = "비공개 답변입니다" if answer_filter.first().flag == 1 else answer_filter.first().content
                flag = answer_filter.first().flag

            book_data = {
                'questionNum': i,
                'question': question.content,
                'answer': content,
                'flag': flag
            }
            questions.append(book_data)

        return Response({'userId': f_id, 'questions': questions})