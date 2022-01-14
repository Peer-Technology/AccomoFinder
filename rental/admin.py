from django.contrib import admin

from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
# Register your models here.

admin.site.register(PaymentMode) 
admin.site.register(Booking) 
admin.site.register(BookingPay)
admin.site.register(Search) 
admin.site.register(rental_listing) 
admin.site.register(tenant_rental) 
admin.site.register(tenant_payment) 
admin.site.register(rental_listing_reviews) 

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

# import json from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin): formfield_overrides = {
#     map_fields.AddressField: { ‘widget’:
#     map_widgets.GoogleMapsAddressWidget(attrs={
#       ‘data-autocomplete-options’: json.dumps({ ‘types’: [‘geocode’,
#       ‘establishment’], ‘componentRestrictions’: {
#                   'country': 'us'
#               }
#           })
#       })
#     },
# }