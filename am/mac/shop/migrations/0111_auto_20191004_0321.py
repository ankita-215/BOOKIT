# Generated by Django 2.0.5 on 2019-10-03 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0110_auto_20191002_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 10, 4), null=True),
        ),
    ]
