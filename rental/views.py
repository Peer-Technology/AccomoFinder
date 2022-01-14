from django.shortcuts import render ,redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from .tables import *
from .filters import *
from django_tables2.config import RequestConfig
from rest_framework.views import APIView
from . tables import *
from django_tables2.export.export import TableExport
# import requests
import json
import http.client
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2.export.export import TableExport
import folium
import geocoder
from .forms import *
def index(request):
    form = SearchForm()
    # prof = profile.objects.get(user=request.user)
    prof = profile.objects.get(user=request.user)
    if prof:
        rental_places = rental_listing.objects.filter(city=prof.city,preference=prof.gender)
    else:
        rental_places = rental_listing.objects.all()
    m = folium.Map(location=[-17.3708521,30.1473976] , zoom_start=13)
    for place in rental_places:
        # folium.Marker([-17.845634, 31.119771] , tooltip="Click for More",popup="Harare").add_to(m)
        # folium.Marker([-17.351682718824286, 30.205762433872952] , tooltip="Click for More",popup="Chinhoyi").add_to(m)
        folium.Marker([place.geom_lat,place.geom_long] , tooltip=place.description,popup=str(place.available_rooms)+ " , $"+ str(place.price_per_room)).add_to(m)
    m = m._repr_html_()
    booking_form = BookingForm()
    context = {
        'form':form,
        'booking_form':booking_form,
        'm':m,
        'rental_places': rental_places,
    }
    # return HttpResponse("Rental Places")
    return render(request, 'rental/index.html', context)

def search(request):
    # address = request.POST.get('address')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rentals/search')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    print(lat)
    print(lng)
    if lat == None or lng == None or country==None:
        address.delete()
        address = Search.objects.all().last()
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        country = location.country
    rental_places = rental_listing.objects.filter(city=address.address)
    
    m = folium.Map(location=[-17.3708521,30.1473976] , zoom_start=13)
    # folium.Marker([-17.845634, 31.119771] , tooltip="Click for More",popup="Harare").add_to(m)
    # folium.Marker([-17.351682718824286, 30.205762433872952] , tooltip="Click for More",popup="Chinhoyi").add_to(m)
    folium.Marker([lat,lng] , tooltip="Click for More",popup=country + " , "+ address.address).add_to(m)
    for place in rental_places:
        # folium.Marker([-17.845634, 31.119771] , tooltip="Click for More",popup="Harare").add_to(m)
        # folium.Marker([-17.351682718824286, 30.205762433872952] , tooltip="Click for More",popup="Chinhoyi").add_to(m)
        folium.Marker([place.geom_lat,place.geom_long] , tooltip=place.description,popup=str(place.available_rooms)+ " , $"+ str(place.price_per_room)).add_to(m)
    m = m._repr_html_()
    context = {
        'form':form,
        'm':m,
        'rental_places': rental_places,
    }
    # return HttpResponse("Rental Places")
    return render(request, 'rental/search.html', context)

def places(request):
    prof = profile.objects.get(user=request.user)
    if prof:
        rental_places = rental_listing.objects.filter(city=prof.city)
    else:
        rental_places = rental_listing.objects.all()
    groups = request.user.groups.all()
    
    myFilter = RentalListingFilter(request.GET,queryset=rental_places)
    rental_places = myFilter.qs
    rental_places_table = RentalListingTable(rental_places)
    RequestConfig(request).configure(rental_places_table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, rental_places_table)
        return exporter.response("table.{}".format(export_format))
    return render(request, 'rental/list.html', {'rental_places': rental_places ,'myFilter':myFilter, 'rental_places_table': rental_places_table})

def add_place(request):
    if request.method == 'POST':
        form = RentalPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            rental_places = rental_listing.objects.all()
            lat = request.POST.get('geom_lat')
            lng = request.POST.get('geom_long')
            organization = request.POST.get('organization')
            address = request.POST.get('address')
            m = folium.Map(location=[-17,32] , zoom_start=10)
            folium.Marker([lat,lng] , tooltip="Click for More",popup=organization + " , "+ address).add_to(m)
            m = m._repr_html_()
            context = {
                'form':form,
                'm':m,
                'rental_places': rental_places,
            }
            # return HttpResponse("Rental Places")
            return render(request, 'rental/index.html', context)
    else:
        form = RentalPlaceForm()
    # rental_places = rental_listing.objects.all()
    # m = folium.Map(location=[-17,31] , zoom_start=6)
    # for place in rental_places:
    #     # folium.Marker([-17.845634, 31.119771] , tooltip="Click for More",popup="Harare").add_to(m)
    #     # folium.Marker([-17.351682718824286, 30.205762433872952] , tooltip="Click for More",popup="Chinhoyi").add_to(m)
    #     folium.Marker([place.geom_lat,place.geom_long] , tooltip=place.description,popup=str(place.available_rooms)+ " , $"+ str(place.price_per_room)).add_to(m)
    # m = m._repr_html_()
    context = {
        'form':form,
        # 'm':m,
        # 'rental_places': rental_places,
    }
    # return HttpResponse("Rental Places")
    return render(request, 'rental/add_place.html', context)

    # https://www.paynow.co.zw/Payment/BillPaymentLink/?q=aWQ9MTMwOTYmYW1vdW50PTUwLjAwJmFtb3VudF9xdWFudGl0eT0wLjAwJmw9MQ%3d%3d


def place_booking(request):
    if request.POST:
        user_id = request.POST.get('user_id')
        place_id = request.POST.get('listing')
        rooms = request.POST.get('number_of_rooms')
        rentallisting = rental_listing.objects.get(id=place_id)
        user_profile = profile.objects.get(user=user_id)
        data = {
            'tenant': user_profile,
            'listing': rentallisting,
            'number_of_rooms': rooms
        }
        bform = BookingForm(data=data)
        if bform.is_valid():
            bform.save()
            return redirect('/')
        # b4_Form = Booking.objects.get(user=request.user)
        # b4_Form.city = request.POST.get('city')
        # b4_Form.nearby_institute = request.POST.get('nearby_institute')
        # b4_Form.save() 
    context = {
    }
    return render(request, 'rental/add_place.html', context)
def pay_booking(request):
    error_message = ""
    success_message = ""
    if request.POST:
        form = BookingPayForm(request.POST)
        bng = request.POST.get('booking')
        booking_listing = Booking.objects.get(id=bng)
        lsng = booking_listing.listing
        print('lsng')
        print(lsng.id)
        if form.is_valid():
            form.save()
            b4_Form = rental_listing.objects.get(id=lsng.id)
            print(b4_Form)
            print('b4_Form.available_rooms - 1')
            print(b4_Form.available_rooms - 1)
            b4_Form.available_rooms = b4_Form.available_rooms - 1
            if b4_Form.save():
                my_profile = profile.objects.get(user=request.user.id)
                my_bookings = Booking.objects.filter(tenant=my_profile)
                print(my_bookings)
                
                myFilter = BookingFilter(request.GET,queryset=my_bookings)
                my_bookings = myFilter.qs
                bookings_table = BookingTable(my_bookings)
                RequestConfig(request).configure(bookings_table)
                export_format = request.GET.get("_export", None)
                if TableExport.is_valid_format(export_format):
                    exporter = TableExport(export_format, bookings_table)
                    return exporter.response("table.{}".format(export_format))
                context = {
                    "bookings_table":bookings_table,
                    "my_bookings": my_bookings,
                    "myFilter": myFilter,
                    "my_profile":my_profile,
                }
                return render(request, 'rental/my_bookings.html', context)
            else:
                error_message = "Data Not Saved"
            
    else:
        form = BookingPayForm()
    context = {
        "form":form,
        "error_message": error_message,
    }
    return render(request, 'rental/pay.html', context)
def my_booking(request):
    my_profile = profile.objects.get(user=request.user.id)
    my_bookings = Booking.objects.filter(tenant=my_profile)
    print(my_bookings)
    
    myFilter = BookingFilter(request.GET,queryset=my_bookings)
    my_bookings = myFilter.qs
    bookings_table = BookingTable(my_bookings)
    RequestConfig(request).configure(bookings_table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, bookings_table)
        return exporter.response("table.{}".format(export_format))
    context = {
        "bookings_table":bookings_table,
        "my_bookings": my_bookings,
        "myFilter": myFilter,
        "my_profile":my_profile,
    }
    return render(request, 'rental/my_bookings.html', context)