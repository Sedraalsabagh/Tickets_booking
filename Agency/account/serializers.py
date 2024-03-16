from rest_framework import serializers
from django.contrib.auth.models import User

class SingUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # استخدام CharField بدلاً من PasswordField

    class Meta:
        model =User
        fields=('first_name','last_name','email','password')

        extra_kword={
            'first_name':{'required':True,'allow_blank':False},
            'last_name':{'required':True,'allow_blank':False},
            'email':{'required':True,'allow_blank':False},
            'password':{'required':True,'allow_blank':False,'min_length':8}

        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=('first_name','last_name','email','password')



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=('username','password')
extra_kword={
             'username':{'required':True,'allow_blank':False},
             'password':{'required':True,'allow_blank':False,'min_length':8}
           
             }