# Generated by Django 2.2.3 on 2019-08-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0071_auto_20190823_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='email',
            field=models.EmailField(default='', max_length=60, unique=True),
        ),
    ]
