from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, DateField, FilePathField, FloatField, IntegerField
from django.contrib.auth.models import User
from api.models import profile
from django_google_maps import fields as map_fields
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Payments/user_{0}/{1}'.format(filename)

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
class PaymentMode(models.Model):
    amount = models.FloatField(default=0, null=True)
    url =models.CharField(blank=True ,max_length=500)
    added_on = models.DateTimeField(auto_now=True)

# Create your models here.
class rental_listing(models.Model):
    LISTING_CHOICES = (
        ('App', 'Apartment'),
        ('FH', 'Full House'),
        ('BC', 'Bachelor Court'),
        ('SC', 'spinster Court'),
        ('SH', 'Sharing'),
    )
    City_CHOICES = (
        ('Mutare', 'Mutare'),
        ('Harare', 'Harare'),
        ('Gweru', 'Gweru'),
        ('Masvingo', 'Masvingo'),
        ('Chinhoyi', 'Chinhoyi'),
        ('Bulawayo', 'Bulawayo'),
        ('Zvishavane', 'Zvishavane'),
    )
    PREF_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Mixed', 'Mixed'),
    )
    home_owner= models.ForeignKey(profile ,on_delete=models.CASCADE)
    organization = models.CharField(blank=True ,max_length=200)
    description = models.TextField(blank=True ,max_length=1000)
    lease_terms = models.TextField(blank=True ,max_length=1000)
    type_of_listing = models.CharField(blank=True ,max_length=200 ,choices = LISTING_CHOICES)
    preference = models.CharField(blank=True ,max_length=200 ,choices = PREF_CHOICES)
    address = models.CharField(blank=True ,max_length=200)
    city = models.CharField(blank=True ,max_length=200, choices = City_CHOICES)
    house_number = models.IntegerField(blank=True, null=True)
    max_rooms = models.IntegerField(default=0 ,null=True)
    vacant = models.BooleanField(default=0 ,null=True)
    wifi = models.BooleanField(default=0 ,null=True)
    solar = models.BooleanField(default=0 ,null=True)
    curfew =models.CharField(blank=True ,max_length=200)
    pets_allowed =models.BooleanField(blank=True ,default=0)
    available_rooms = models.IntegerField(default=0 ,null=True)
    price_per_room = models.FloatField(default=0, null=True)
    price_total = models.FloatField(default=0, null=True)
    geom_lat = models.FloatField(default=0 ,null=True)
    geom_long = models.FloatField(default=0 ,null=True)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.address 

class tenant_rental(models.Model):
    tenant= models.ForeignKey(profile ,on_delete=models.CASCADE)
    listing = models.ForeignKey(rental_listing ,on_delete=models.CASCADE)
    staying_period_from = models.DateField(null=True)
    staying_period_to = models.DateField(null=True)
    confirmed = BooleanField(default=0 ,null=True)
    evicted = BooleanField(default=0 ,null=True)
    moved = BooleanField(default=0 ,null=True)
    lease_start_date = DateField(null=True)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tenant.user.username

class tenant_payment(models.Model):
    LISTING_CHOICES = (
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    )
    listing = models.ForeignKey(tenant_rental ,on_delete=models.CASCADE)
    paid_by= models.ForeignKey(profile ,on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=0 ,null=True)
    balance = models.FloatField(default=0 ,null=True)
    paid_for_month = models.CharField(blank=True ,max_length=200 ,choices = LISTING_CHOICES)
    paid_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.paid_by.user.username

class rental_listing_reviews(models.Model):
    reviewed_by= models.ForeignKey(profile ,on_delete=models.CASCADE)
    listing = models.ForeignKey(rental_listing ,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0 ,null=True)
    comment = models.IntegerField(default=0 ,null=True)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.reviewed_by.user.username

class Search(models.Model):
    address= models.CharField(blank=True ,max_length=200 ,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address

class Booking(models.Model):
    tenant= models.ForeignKey(profile ,on_delete=models.CASCADE)
    listing = models.ForeignKey(rental_listing ,on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField(default=0 ,null=True)
    approved = BooleanField(default=0 ,null=True)
    rejected = BooleanField(default=0 ,null=True)
    waiting_list = BooleanField(default=0 ,null=True)
    date_of_booking = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tenant.user.username

class BookingPay(models.Model):
    payment_made_by= models.ForeignKey(User ,on_delete=models.CASCADE)
    booking= models.ForeignKey(Booking ,on_delete=models.CASCADE)
    proof_of_payment_attached = BooleanField(default=0 ,null=True)
    # file = models.FileField(upload_to=user_directory_path ,null=True)
    amount = models.FloatField(null=True)
    date_of_payment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking.tenant.user.username