# Generated by Django 2.2.3 on 2019-08-22 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0068_auto_20190822_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Cat'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.scat'),
        ),
    ]
