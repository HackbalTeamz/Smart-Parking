# Generated by Django 3.1.4 on 2021-01-16 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_vendor', '0005_auto_20210116_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='cdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
