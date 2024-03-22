from rest_framework import serializers
from .models import User,UserProfile

class SingUpSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields=('first_name','last_name','email','password')

        extra_kword={
            'first_name':{'required':True,'allow_blank':False},
            'last_name':{'required':True,'allow_blank':False},
            'email':{'required':True,'allow_blank':False},
            'password':{'required':True,'allow_blank':False,'min_length':8}

        }


#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model =User
   #     fields=('first_name','last_name','email','password')



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=('username','password')
extra_kword={
             'username':{'required':True,'allow_blank':False},
             'password':{'required':True,'allow_blank':False,'min_length':8}
           
             }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserProfile
        fields=('date_of_birth','gender','address')

        extra_kword={
            
             'age':{'required':True,'allow_blank':False},
              
              'address':{'required':True,'allow_blank':False},
           
             }