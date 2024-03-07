from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
 
     class Meta:
        model=Flight
        fields="__all__"
``
#class ReviewSerializer(serializers.ModelSerializer):

 #   class Meta:
  #      model=Review
   #     fields="__all__"
