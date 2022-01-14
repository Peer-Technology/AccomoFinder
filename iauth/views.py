from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import request
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from django.contrib.auth.models import User,Group
from rental.models import *
from api.models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
from django.db.models import Q

@login_required
def dashboard(request):
    my_places = []
    groups = request.user.groups.all()
    system_groups = Group.objects.all()
    # Entry.objects.filter(~Q(id=3))
    my_profile = profile.objects.get(user=request.user.id)
    rental_places = rental_listing.objects.filter(~Q(available_rooms=0),preference=my_profile.gender)

    my_bookings = Booking.objects.filter(tenant=my_profile)
    my_payments = BookingPay.objects.filter(payment_made_by=request.user)
    for group in groups:
        # print("Group XX")
        # print(group.name)
        if group.name == "Agent" or group.name == "Owner":
            my_places = rental_listing.objects.filter(home_owner=request.user.id)
        else:
            my_places = []
    context = {
        "my_payments":my_payments,
        "my_bookings":my_bookings,
        "rental_places":rental_places,
        "my_places": my_places,
        "system_groups":system_groups,
        "groups": groups,
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'iauth/dashboard.html', context=context)


@login_required
def myprofile(request):
    prof = profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            b4_Form = profile.objects.get(user=request.user)
            b4_Form.city = request.POST.get('city')
            b4_Form.nearby_institute = request.POST.get('nearby_institute')
            b4_Form.save() 
            # form.update()
            return HttpResponse("Data Saved Successfully")
        else:
            return HttpResponse("Form Is not valid")
    else:            
        profile_form = ProfileForm(instance=request.user)  
    groups = request.user.groups.all()
    context = {
        "prof":prof,
        "groups":groups,
        "profile_form": profile_form,
        "welcome": "Welcome to your profile"
    }
    return render(request, 'iauth/profile.html', context=context)



def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'iauth/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'iauth/register.html', context=context)


@login_required
def edit(request):
    prof = ""
    system_groups = ""
    groups = request.user.groups.all()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        mygrp= request.POST.get('my_grp')
        g = Group.objects.get(name=mygrp)
        u = request.user
        g.user_set.add(u)
        if user_form.is_valid():
            user_form.save()
    else:
        prof = request.GET['profile']
        system_groups = Group.objects.get(name=prof)
        user_form = UserEditForm(instance=request.user)
    context = {
        "system_groups":system_groups,
        "prof":prof,
        'form': user_form,
       "groups": groups,
    }
    return render(request, 'iauth/edit.html', context=context)
