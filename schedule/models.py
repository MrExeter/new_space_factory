from django.db import models
from vehicle_order.models import VehicleOrder


# class VehicleComponent(models.Model):
#     name = models.CharField(max_length=36)
#     part_number = models.CharField(max_length=64, unique=True)
#     quantity = models.IntegerField(default=1)
#
#     # This is the time required to process or "integrate" this into the vehicle
#     process_time = models.IntegerField(default=1)
#
#     def __str__(self):
#         return self.name


# class Bom(models.Model):
#     name = models.CharField(max_length=36)
#     tracking_code = models.CharField(max_length=36)
#     description = models.CharField(max_length=128)
#     vehicle_parts = models.ManyToManyField(VehicleComponent)
#
#     def __str__(self):
#         return self.name


# class VehicleOrder(models.Model):
#
#     name = models.CharField(max_length=36)
#     order_code = models.CharField(max_length=64, unique=True)
#     description = models.CharField(max_length=64)
#     created_date = models.DateTimeField(default=now, editable=False)
#     start_date = models.DateTimeField(default=now)
#     estimated_complete_date = models.DateTimeField()
#
#     bill_of_materials = models.OneToOneField(Bom, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name







class Schedule(models.Model):
    name = models.CharField(max_length=36)
    on_schedule = models.BooleanField(default=True)

    vehicle_order = models.ForeignKey(VehicleOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " : " + self.vehicle_order.order_code + \
               " : on schedule : " + str(self.on_schedule)
