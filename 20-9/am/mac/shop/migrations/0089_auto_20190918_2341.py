# Generated by Django 2.2.3 on 2019-09-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0088_auto_20190918_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='Mono',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Pincode',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='adharcard',
            field=models.FileField(default='', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='policeverification',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
