# Generated by Django 2.0.4 on 2018-05-21 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_auto_20180520_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='admin_adittions',
        ),
        migrations.RemoveField(
            model_name='office',
            name='admin_settings',
        ),
    ]
