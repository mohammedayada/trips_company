# Generated by Django 3.1.7 on 2021-03-11 01:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='start_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 1, 31, 11, 443238, tzinfo=utc)),
        ),
    ]
