from django.core.mail import send_mail, BadHeaderError
from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.urls import path, include
from django.shortcuts import redirect, render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from api.models import *
from rental.models import *
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("API EndPoints")


@login_required
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer

class RentalListingViewSet(viewsets.ModelViewSet):
    queryset = rental_listing.objects.all()
    serializer_class = RentalListingSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class PaymentModeViewSet(viewsets.ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer
