from django.db import models
from bom.models import Bom
from datetime import datetime
from django.utils.timezone import now


class VehicleOrder(models.Model):

    name = models.CharField(max_length=36)
    order_code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=now, editable=False)
    start_date = models.DateTimeField(default=now)
    estimated_complete_date = models.DateTimeField()

    bill_of_materials = models.OneToOneField(Bom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
