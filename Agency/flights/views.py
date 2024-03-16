from django.shortcuts import render
from django.shortcuts import render,get_object_or_404 
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .models import Flight,Airline
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
from .serializer import FlightSerializer
from .filters import FlightsFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
@api_view(['GET'])
def get_all_flights(request) :
    flights=Flight.objects.all()
    serializer=FlightSerializer(flights,many=True)
    print(flights)
    return Response({"flights":serializer.data}) 


@api_view(['POST'])
def get_by_id_flights(request,pk) :
    flights = get_object_or_404(Flight, id=pk)
    serializer=FlightSerializer(flights,many=False)
    print(flights)
    return Response({"flights":serializer.data})   


@api_view(['GET'])
def get_all(request) :
    filterset=FlightsFilter(request.GET,queryset=Flight.objects.all().order_by('id'))
    serializer=FlightSerializer(filterset.qs ,many=True)
    return Response({"flights":serializer.data})




'''
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # بس الموظف يلي عامل ريجستر بيقدر يضيف رحلات
def new_flight(request) :
    data=request.data
    serializer=FlightSerializer(data=data)
    
    if serializer.is_valid():
    
       airline_id = data.pop('airline')  # Extract airline ID from request data
       flights=Flight.objects.create(**data,Employee=request.Employee)
       req=FlightSerializer(Flight,many=False)

       return Response({"flights":req.data})   


    else: 
       return   Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

'''



@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
        
        rating=flight.reviws.aggregate(avg_ratings=Avg('rating'))
        flight.ratings=rating['avg_ratings']
        flight.save()
        return Response({'details':'Flight review updated'})
    else:
            Review.objects.create(
                user=user,
                flight=flight,
                rating=data['rating'],
                comment=data['comment']
            )
            rating=flight.reviews.aggregate(avg_ratings=Avg('rating'))
            flight.ratings=rating['avg_ratings']
            flight.save()
            return Response({'details':'flight review created'})


@api_view
@permission_classes([IsAuthenticated])
def delete_review(request,pk):
    user=request.user
    flight=get_object_or_404(Flight,id=pk)
    review=flight.reviews.filter(user=user)

    if review.exists():
        review.delete|()
        rating=flight.reviews.aggregate(avg_ratings=Avg('rating'))
        if  rating['avg_ratings'] is None:
         rating['avg_ratings'] =0
         flight.ratings=rating['avg_ratings']
         flight.save()
         return Response({'details':'flight review deleted'})

    else:
        return Response({'error':'Review not found'},status=status.HTTP_404_NOT_FOUND)


