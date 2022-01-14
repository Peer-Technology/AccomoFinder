from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import Group

class profile(models.Model):
    City_CHOICES = (
        ('Mutare', 'Mutare'),
        ('Harare', 'Harare'),
        ('Gweru', 'Gweru'),
        ('Masvingo', 'Masvingo'),
        ('Chinhoyi', 'Chinhoyi'),
        ('Bulawayo', 'Bulawayo'),
        ('Zvishavane', 'Zvishavane'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('--', '--'),
    )
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    # bio = models.CharField(blank=True ,max_length=200)
    # age = models.CharField(blank=True ,max_length=200)
    # sex = models.CharField(blank=True ,max_length=200)
    # phone = models.CharField(blank=True ,max_length=200)
    # current_address = models.CharField(blank=True ,max_length=200)
    city = models.CharField(blank=True ,max_length=200, choices = City_CHOICES)
    gender = models.CharField(blank=True ,max_length=100, choices = GENDER_CHOICES)
    # dob = models.DateField(null=True, blank=True)
    nearby_institute = models.CharField(blank=True ,max_length=200)
    def __str__(self):
        return self.user.username

@receiver(post_save ,sender=User)
def create_user_profile(sender , instance , created , **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save , sender=User)
def save_user_profile(sender , instance , **kwargs):
    instance.profile.save()
