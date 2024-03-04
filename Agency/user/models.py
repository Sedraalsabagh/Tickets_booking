from django.db import models

# Create your models here.









class Customer(model.Models):
    user_id=models.IntegerField(max_length=10),
    phone=models.CharField(max_length=20),
    address=models.CharField(max_length=30),
    gender=models.CharField(max_length=20),
    passport_number=models.IntegerField(max_length=30),