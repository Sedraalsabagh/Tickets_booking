from rest_framework import serializers
from .models import Flight,Review

class FlightSerializer(serializers.ModelSerializer) :
    
    reviws=serializers.SerializerMethodField(method_name='get_reviews',read_only=True)
    class Meta:
        model=Flight
        fields="all"

    

    def get_reviews(self,obj):
        reviews=obj.reviews.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data
    
class ReviewSerializer(serializers.ModelSerializer) : 
    class Meta:
       
        model=Review
        fields="all"

class FlightSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model=Flight
        fields=['return_date','duration','notes','ratings']        






'''
class FlightSerializerRating(serializers.ModelSerializer):

     class Meta:
         model=Flight
         fields=('flight_id','notes')       
class RatingSerializer(serializers.ModelSerializer):

    class Meta :
        model=Rating
        fields=('id','flight','user','star')       
'''