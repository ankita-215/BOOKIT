# Generated by Django 2.2.3 on 2019-08-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=12)),
                ('email', models.EmailField(default='', max_length=60, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='admin',
        ),
    ]
