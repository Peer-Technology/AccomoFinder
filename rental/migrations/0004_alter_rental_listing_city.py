# Generated by Django 3.2.3 on 2022-01-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_rental_listing_price_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_listing',
            name='city',
            field=models.CharField(blank=True, choices=[('Mutare', 'Mutare'), ('Harare', 'Harare'), ('Chinhoyi', 'Chinhoyi')], max_length=200),
        ),
    ]
