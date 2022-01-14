from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.urls import path, include
from django.shortcuts import render
from rental.models import *
from .models import *
# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']
class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = ['amount', 'url']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        depth=6

        fields = ['user', 'city','gender', 'nearby_institute']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        depth=6
        fields = [
            'tenant',
            'listing',
            'number_of_rooms',
            'approved',
            'rejected',
            'waiting_list',
            'date_of_booking',
            ]

class RentalListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rental_listing
        depth=6
        fields = [
                'id',
                'home_owner',
                'organization',
                'description',
                'lease_terms',
                'type_of_listing',
                'address',
                'city',
                'house_number',
                'preference',
                'max_rooms',
                'vacant',
                'wifi',
                'solar',
                'curfew',
                'pets_allowed',
                'available_rooms',
                'price_per_room',
                'geom_lat',
                'geom_long',
                'added_on',
            ]