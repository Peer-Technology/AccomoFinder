# Generated by Django 3.2.3 on 2022-01-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0013_auto_20220109_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_rooms',
            field=models.IntegerField(default=0, null=True),
        ),
    ]