# Generated by Django 2.2.3 on 2019-07-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20190731_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='email',
            field=models.EmailField(default='', max_length=60, unique=True),
        ),
    ]
