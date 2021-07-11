# Generated by Django 3.1.4 on 2021-07-11 08:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property_vendor', '0013_auto_20210409_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('reportedby', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
