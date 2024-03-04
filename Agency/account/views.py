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
    