# Generated by Django 2.1.7 on 2019-03-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_component', '0005_vehiclecomponent_facility_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclecomponent',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
    ]