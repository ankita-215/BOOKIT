# Generated by Django 2.2.3 on 2019-09-16 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0079_auto_20190913_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='document',
            field=models.FileField(default='', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='enddate',
            field=models.DateField(blank=True, default=datetime.date(2019, 9, 16), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 9, 16), null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 9, 16), null=True),
        ),
    ]
