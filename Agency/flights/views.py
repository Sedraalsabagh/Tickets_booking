from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer 

# Create your views here.
@api_view(['GET'])
def get_all_flights(request) :
    #filterset=FlightsFilter(request.GET,queryset=Flight.object.all().order_by('id'))
    flights=Flight.objects.all()
    filterset=FlightFilter(request.GET,queryset=Flight.object.all().order_by('id'))
    #serializer=FlightSerializer(flights,many=True)
    serializer=FlightSerializer(filterset.qs,many=True)

    #print(flights)
    #return Response({"flights":serializer.data})
    return Response({"flights":serializer.data})


@api_view(['GET'])
def get_by_id_flights(request,pk) :
    #filterset=FlightsFilter(request.GET,queryset=Flight.object.all().order_by('id'))
    flights=get.object_or_404(Flight,id=pk)
    serializer=FlightSerializer(flights,many=False)
    print(flights)
    #return Response({"flights":serializer.data})
    return Response({"flight":serializer.data})