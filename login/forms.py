from django import forms
from django.contrib.auth.forms import UserCreationForm
from login.models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['user_id', 'password', 'nickname', 'code']  # 필드를 적절히 조정하세요.
