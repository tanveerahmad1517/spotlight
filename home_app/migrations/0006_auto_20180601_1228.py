# Generated by Django 2.0.4 on 2018-06-01 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_auto_20180521_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeworkers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]