# Generated by Django 2.2.3 on 2019-08-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20190810_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=60),
        ),
    ]
