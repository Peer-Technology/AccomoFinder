# Generated by Django 3.2.3 on 2022-01-09 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0016_auto_20220109_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpay',
            name='date_of_payment',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
