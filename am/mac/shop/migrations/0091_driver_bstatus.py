# Generated by Django 2.2.3 on 2019-09-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0090_auto_20190919_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='bstatus',
            field=models.IntegerField(default=0),
        ),
    ]
