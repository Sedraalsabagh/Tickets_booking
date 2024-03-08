from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer 
from rest_framework.pagination import PageNumberPagination
# Create your views here.
@api_view(['GET'])
def get_all_flights(request) :
    filterset=FlightFilter(request.GET,queryset=Flight.object.all().order_by('id'))
    resPage=2
    paginator=pageNumberPagination()
    pageinator.page_size=resPage
    queryset=paginator.paginate_queryset(filterset.qs,request)
    #filterset=FlightsFilter(request.GET,queryset=Flight.object.all().order_by('id'))
    flights=Flight.objects.all()
    #serializer=FlightSerializer(flights,many=True)
    serializer=FlightSerializer(queryset,many=True)

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