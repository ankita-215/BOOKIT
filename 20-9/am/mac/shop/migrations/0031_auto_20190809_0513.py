# Generated by Django 2.2.3 on 2019-08-08 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20190809_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='enddate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 9, 5, 13, 10, 5162)),
        ),
    ]
