from django.contrib import auth
from django.contrib.auth import logout
from django.views import View
from login.models import Member
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date

# 회원 가입
class SignUp(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    
    # id 중복 확인을 위한 메소드
    @api_view(['POST'])
    def check_duplicate_user(request):
        user_id=request.data.get('user_id')
        try:
            Member.objects.get(user_id=user_id)
            return Response({'success': False, 'message': '이미 존재하는 사용자 ID입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return Response({'success': True, 'message': '사용 가능한 사용자 ID입니다.'}, status=status.HTTP_200_OK)

    # 회원 가입을 위한 메소드
    @api_view(['POST'])
    def signup(request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        code = request.data.get('code')
        startdate = date.today()
        if user_id and password and nickname and code:
            try:
                existing_user = Member.objects.get(user_id=user_id)
                return Response({'success':False},status=status.HTTP_400_BAD_REQUEST)
            except Member.DoesNotExist:
                member = Member.objects.create(user_id = user_id,password=password,nickname=nickname,code=code,startdate=startdate)
                member.save()
                return Response({'success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'success':False},status=status.HTTP_400_BAD_REQUEST)

# 로그인
class Login(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    @api_view(['POST'])
    def login(request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        
        if Member.objects.filter(user_id=user_id).exists():
            getMember = Member.objects.get(user_id=user_id)
            if getMember.password == password:
                return Response({'success': True, 'message': '로그인 되었습니다.'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': '비밀번호가 틀렸습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'message': '존재하지 않는 ID입니다.'}, status=status.HTTP_400_BAD_REQUEST)
