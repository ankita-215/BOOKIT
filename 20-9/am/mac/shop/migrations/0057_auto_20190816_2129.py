# Generated by Django 2.2.3 on 2019-08-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_auto_20190816_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='C',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dp',
            field=models.CharField(max_length=13),
        ),
    ]
