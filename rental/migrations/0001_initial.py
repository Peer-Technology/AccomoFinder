# Generated by Django 3.2.3 on 2021-12-09 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rental_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('lease_terms', models.TextField(blank=True, max_length=1000)),
                ('type_of_listing', models.CharField(blank=True, choices=[('App', 'Apartment'), ('FH', 'Full House'), ('BC', 'Bachelor Court'), ('SC', 'spinster Court'), ('SH', 'Sharing')], max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('house_number', models.IntegerField(blank=True, null=True)),
                ('max_rooms', models.IntegerField(default=0, null=True)),
                ('vacant', models.BooleanField()),
                ('available_rooms', models.IntegerField(default=0, null=True)),
                ('price_per_room', models.FloatField(default=0, null=True)),
                ('geom_lat', models.BigIntegerField(default=0, null=True)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('home_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='tenant_rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staying_period_from', models.DateField(null=True)),
                ('staying_period_to', models.DateField(null=True)),
                ('confirmed', models.BooleanField(default=0, null=True)),
                ('evicted', models.BooleanField(default=0, null=True)),
                ('moved', models.BooleanField(default=0, null=True)),
                ('lease_start_date', models.DateField(null=True)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rental_listing')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='tenant_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField(default=0, null=True)),
                ('balance', models.FloatField(default=0, null=True)),
                ('paid_for_month', models.CharField(blank=True, choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=200)),
                ('paid_on', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.tenant_rental')),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='rental_listing_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, null=True)),
                ('comment', models.IntegerField(default=0, null=True)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rental_listing')),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]