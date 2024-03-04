from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password 
from rest_framework import status
from .serializers import SingUpSerializer

# Create your views here.

@api_view
def register(request):
    data=request.data
    user=SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data('email')).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=make_password(data['password']),
            )