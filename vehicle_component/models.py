from django.db import models


class VehicleComponent(models.Model):
    name = models.CharField(max_length=36)
    part_number = models.CharField(max_length=64, unique=True)
    quantity = models.IntegerField(default=1)

    # This is the time required to process or "integrate" this into the vehicle
    process_time = models.IntegerField(default=1)

    def __str__(self):
        return self.name
