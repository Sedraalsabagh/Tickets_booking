import django_filters
from .models import Flight


class FlightsFilter(django_filters.FilterSet):
    departure_airport = django_filters.CharFilter(field_name='airportDeparture', label='Departure Airport', lookup_expr='exact', required=True)
    arrival_airport = django_filters.CharFilter(field_name='airportArrival', label='Arrival Airport', lookup_expr='exact', required=True)
    airline = django_filters.CharFilter(field_name='airline_name', label='Airline', lookup_expr='icontains')

    class Meta:
       model = Flight
       fields = ['airportDeparture', 'airportArrival']

    def filter_queryset(self, queryset):
        if self.data.get('airportDeparture') and self.data.get('airportArrival'):
            return super().filter_queryset(queryset)
        else:
            return queryset.none()



        