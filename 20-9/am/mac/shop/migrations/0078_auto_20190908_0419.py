# Generated by Django 2.2.3 on 2019-09-07 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0077_auto_20190908_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='id',
            new_name='did',
        ),
    ]
