from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login.models import Member

class LoginForm(forms.Form):
    user_id = forms.CharField(label='사용자 ID', max_length=30)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

