from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password 
from rest_framework import status
from .serializers import SingUpSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated #لحماية المسارات
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth.models import User

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
            #user.save()
             


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
   

@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
           
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    



               
@api_view(['GET'])          
@permission_classes([IsAuthenticated])       
def current_user(request):
  user=UserSerializer(request.user)
  return Response(user.data)









  