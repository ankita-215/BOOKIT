# Generated by Django 2.2.3 on 2019-08-09 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='enddate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 10), null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 10), null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 10), null=True),
        ),
    ]
