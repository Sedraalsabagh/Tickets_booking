from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.




class User(AbstractUser) :
    
    
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=128,unique=True)
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    #USERNAME-FIELD=='email',

class Customer(models.Model):
        GUNDER_CHOICES=(
        (1,'male'),
        (2,'femail'),
       
    )
        user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
        phone_number=models.CharField(max_length=20,blank=True,null=True)
        location=models.CharField(max_length=40,blank=True,null=True)
        passport_number=models.CharField(max_length=100,blank=True,null=True)
        gender=models.SmallIntegerField(choices=GUNDER_CHOICES,null=True)

class Employee(models.Model):
        user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
        phone_number=models.CharField(max_length=20,blank=True,null=True)
        location=models.CharField(max_length=40,blank=True,null=True)