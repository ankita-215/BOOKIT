# Generated by Django 2.0.5 on 2019-09-27 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0099_auto_20190928_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 9, 28), null=True),
        ),
    ]
