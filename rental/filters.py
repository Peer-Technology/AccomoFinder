from django.db.models import fields
import django_filters
from django_filters import DateFilter ,CharFilter

from .models import *

class RentalListingFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="start_date" ,lookup_expr="gte")
    # end_date = DateFilter(field_name="end_date" ,lookup_expr="lte")
    lease_terms = CharFilter(field_name="lease_terms" )
    class Meta:
        model = rental_listing
        fields = '__all__'
        exclude = [ 
            'max_rooms',
            'description',
            'lease_terms',
            'curfew',
            'organization',
            'home_owner',
            'address',
            'house_number',
            'geom_lat',
            'geom_long',
            'added_on',
            'price_total',
        ]
class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = [ 
            
        ]
