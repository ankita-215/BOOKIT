# Generated by Django 2.2.3 on 2019-08-07 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20190806_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Rdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 4, 59, 16, 348440)),
        ),
    ]
