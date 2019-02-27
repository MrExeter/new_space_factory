from django.db import models
from vehicle_order.models import VehicleOrder


class Schedule(models.Model):
    name = models.CharField(max_length=36)
    on_schedule = models.BooleanField(default=True)

    vehicle_order = models.ForeignKey(VehicleOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " : " + self.vehicle_order.order_code + \
               " : on schedule : " + str(self.on_schedule)
