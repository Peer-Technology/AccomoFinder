# Generated by Django 3.2.3 on 2022-01-09 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0015_alter_bookingpay_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingpay',
            name='file',
        ),
        migrations.AddField(
            model_name='bookingpay',
            name='payment_made_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
