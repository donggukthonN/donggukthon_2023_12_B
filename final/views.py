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

# class Profile