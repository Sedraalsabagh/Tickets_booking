import django_filters
from .models import Flight,FlightSeatClass


class FlightsFilter(django_filters.FilterSet):
    departure_airport = django_filters.CharFilter(field_name='airportDeparture', label='Departure Airport', lookup_expr='exact', required=True)
    arrival_airport = django_filters.CharFilter(field_name='airportArrival', label='Arrival Airport', lookup_expr='exact', required=True)
    departure_date = django_filters.DateTimeFilter(field_name='departure_date', label='Departure Time', lookup_expr='exact', required=True)
    return_date = django_filters.DateTimeFilter(field_name='departure_date', label='Return Time', lookup_expr='exact', required=True)
    
    class Meta:
       model =Flight
       fields = ['airportDeparture', 'airportArrival','departure_date','return_date']

    def filter_queryset(self, queryset):
        if self.data.get('airportDeparture') and self.data.get('airportArrival') and self.data.get('departure_date') and self.data.get('return_date') :
            return super().filter_queryset(queryset)
        else:
            return queryset.none()