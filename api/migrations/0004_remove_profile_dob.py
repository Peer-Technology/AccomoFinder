# Generated by Django 3.2.3 on 2022-01-08 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_profile_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]
