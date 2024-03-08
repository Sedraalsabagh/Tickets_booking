import django_filters
from .models import Flight


class FlightFilter(django_filters.FilterSet):
    name=django_filters/CharFilter(lookup_exp='iexact')

    class Meta:
        model=Flight
        field=['airportArrival','airportDeparture']