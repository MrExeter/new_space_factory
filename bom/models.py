from django.db import models
from vehicle_component.models import VehicleComponent


class Bom(models.Model):
    """Bill of materials class, represents a list of parts or components"""
    name = models.CharField(max_length=36)
    tracking_code = models.CharField(max_length=36)
    description = models.CharField(max_length=128)
    vehicle_parts = models.ManyToManyField(VehicleComponent)

    def __str__(self):
        return self.name
