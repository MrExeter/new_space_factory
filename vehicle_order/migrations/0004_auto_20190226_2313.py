# Generated by Django 2.1.7 on 2019-02-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_order', '0003_auto_20190226_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleorder',
            name='estimated_complete_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
