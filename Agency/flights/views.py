from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight
from .serializer import FlightSerializer 
from rest_framework.pagination import PageNumberPagination
from .filters import FlightsFilter

@api_view(['GET'])
def get_all_flights(request):
    filterset = FlightsFilter(request.GET, queryset=Flight.objects.all().order_by('id'))
    resPage = 2
    paginator = PageNumberPagination()
    paginator.page_size = resPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = FlightSerializer(queryset, many=True)
    return Response({"flights": serializer.data})

@api_view(['GET'])
def get_by_id_flights(request, pk):
    flight = Flight.objects.get(pk=pk)
    serializer = FlightSerializer(flight, many=False)
    return Response({"flight": serializer.data})
