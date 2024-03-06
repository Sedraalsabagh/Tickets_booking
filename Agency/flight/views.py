from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filtters import FlightsFilter
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
# Create your views here.

@api_view
def get_all_flight(request):

 filterset=Flight(request.GET,queryset=Flight.object.all().order_by('id'))
 count=filterset.qs.coun()
 resPage=2
 

@api_view(['POST'])
@permission_class([IsAuthentication])
def create_review(request,pk):
    user=request.user
    flight=get_object_or_404(Flight,id=pk)
    data=request.data
    review=flight.reviews.filter(user=user)
    
    if data['rating']<=0 or data['rating']>5:
        flight=Flight.object.create(**data,user=request.user)
        res=FlightSerializer(flight,many=False)
        
        return Response({"error":'please select between 1 to 5 only'},status=status.HTTP_400_BAD_REQUEST)
    elif review.exists():
        new_review={'rating':data['rating'],'comment':data['comment']}
        review.update(**new_review)
        
        rating=flight.reviws.aggregate(avg_rating=Avg('rating'))
        flight.rating=rating['avg_ratings']
        flight.save()
        return Response({'details':'Flight review updated'})
    else:
            Review.object.create(
                user=user,
                flight=flight,
                rating=data['rating'],
                comment=datae['comment']
            )
