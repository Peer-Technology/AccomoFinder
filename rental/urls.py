from django.urls import path

from . import views
app_name = 'rental'
urlpatterns = [
    path('', views.index, name='index'),
    path('places', views.places, name='places'),
    path('add_place', views.add_place, name='add_place'),
    path('search', views.search, name='search'),
    path('place_booking', views.place_booking, name='place_booking'),
    path('my_booking', views.my_booking, name='my_booking'),
    path('pay_booking', views.pay_booking, name='pay_booking'),
    
]