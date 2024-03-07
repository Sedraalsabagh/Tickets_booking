import django_filters
from .models import Flight  

class FlightsFilter(django_filters.Filterset)
   name=django_filters.CharFilter(lookup_expr='iexact')
  
   class Meta :
      model=Flight
      field=['airportDeparture','airportArrival'] ## صفصف هي بدنا نتناقش فيها 

      
