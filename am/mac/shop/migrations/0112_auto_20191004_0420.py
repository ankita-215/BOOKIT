# Generated by Django 2.0.5 on 2019-10-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0111_auto_20191004_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverbooking',
            name='p',
        ),
        migrations.AddField(
            model_name='driverbooking',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
