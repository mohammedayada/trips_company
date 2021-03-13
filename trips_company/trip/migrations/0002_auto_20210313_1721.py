# Generated by Django 3.1.7 on 2021-03-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
        ('driver', '0001_initial'),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='bus',
            field=models.ManyToManyField(to='bus.Bus'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.ManyToManyField(to='driver.Driver'),
        ),
    ]