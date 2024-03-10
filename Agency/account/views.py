from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password 
from rest_framework import status
from .serializers import SingUpSerializer
from rest_framework.permissions import IsAuthenticated #لحماية المسارات
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def register(request):
    data=request.data
    user=SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                password=make_password(data['password']),
            )
            return Response(
                {'details':'Your account registered successfully'},
               
                status=status.HTTP_201_CREATED
                
                )
        else:
            return Response(
                {'error':'This email already exists!'},
               
                status=status.HTTP_400_BAD_REQUEST
                  )

    else:
        return Response(user.errors)
   
               
@api_view(['GET'])          
@permission_classes([IsAuthenticated])       
def current_user(request):
  user=SingUpSerializer(request.user)
  return Response(user.data)





  