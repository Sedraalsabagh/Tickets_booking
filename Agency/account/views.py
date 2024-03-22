from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password 
from rest_framework import status
from .serializers import SingUpSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated #لحماية المسارات
from .models import User,UserProfile
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth.models import User
from .form import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@api_view(['POST'])
def register(request):
    data=request.data
    user=SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['username']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=make_password(data['password']),
            )
            user.save()
            #create the user profile
            UserProfile.objects.create(user=user)


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



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_profile(request):
    user_profile = None

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None

    if request.method == 'GET':
        if user_profile:
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        else:
            return Response("Profile does not exist", status=404)
        
    elif request.method in ['POST', 'PUT']:
        if isinstance(request.user, User):
            serializer = UserProfileSerializer(data=request.data, instance=user_profile)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response("User is not authenticated", status=401)

    elif request.method == 'DELETE':
        if user_profile:
            user_profile.delete()
            return Response("Profile deleted successfully")
        else:
            return Response("Profile does not exist", status=404)

    else:
        return Response("Method not allowed", status=405)




'''
@login_required
def edit(request):
   if request.method == 'POST':
      user_form = UserEditForm(instance=request.user,
                                data=request.POST)
      profile_form = ProfileEditForm(
                   instance=request.user.profile,
                   data=request.POST,
                   files=request.FILES)
       if user_form.is_valid() and profile_form.is_valid():
         user_form.save()
         profile_form.save()
  else:
       user_form = UserEditForm(instance=request.user)
       profile_form = ProfileEditForm(
                   instance=request.user.profile)
 '''