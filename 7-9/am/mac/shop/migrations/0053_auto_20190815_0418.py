# Generated by Django 2.2.3 on 2019-08-14 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0052_auto_20190815_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pd',
            old_name='pid',
            new_name='dist',
        ),
        migrations.AddField(
            model_name='booking',
            name='dp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.pd'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='City',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.District'),
        ),
    ]
