# Generated by Django 3.2.10 on 2022-01-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0018_rental_listing_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental_listing',
            name='curfew',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='rental_listing',
            name='solar',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='rental_listing',
            name='wifi',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listing',
            name='vacant',
            field=models.BooleanField(default=0, null=True),
        ),
    ]
