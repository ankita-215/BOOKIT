# Generated by Django 2.2.3 on 2019-08-08 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_register_rdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('Mono', models.CharField(default='', max_length=13)),
                ('City', models.CharField(choices=[('ahemdabad', 'ahemdabad'), ('baroda', 'baroda'), ('rajkot', 'rajkot'), ('junagadh', 'junagadh'), ('amreli', 'amreli')], default='', max_length=20)),
                ('Pincode', models.CharField(default='', max_length=6)),
                ('email', models.EmailField(default='', max_length=60, unique=True)),
                ('o_name', models.CharField(max_length=50)),
                ('v_num', models.CharField(max_length=300, unique=True)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('startdate', models.DateTimeField(default=datetime.datetime.now)),
                ('enddate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 5, 45, 42, 599584)),
        ),
    ]
