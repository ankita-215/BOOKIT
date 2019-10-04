# Generated by Django 2.2.3 on 2019-09-18 22:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0089_auto_20190918_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 9, 19), null=True),
        ),
        migrations.CreateModel(
            name='dbook',
            fields=[
                ('db', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('Mono', models.CharField(default='', max_length=13)),
                ('email', models.EmailField(default='', max_length=60)),
                ('Pincode', models.CharField(default='', max_length=6)),
                ('startdate', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('enddate', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('amount', models.FloatField(default=1.0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.C')),
                ('did', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.driver')),
                ('p', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.P')),
            ],
        ),
    ]
