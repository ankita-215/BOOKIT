# Generated by Django 2.2.3 on 2019-08-14 21:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0051_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='enddate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 15), null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 15), null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Rdate',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 15), null=True),
        ),
        migrations.CreateModel(
            name='pd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.District')),
            ],
        ),
    ]
