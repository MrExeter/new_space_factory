from django.db import models

PRODUCTION_TYPE = (
    ('A', 'Assembly'),
    ('B', 'Electronics'),
    ('C', 'Machining'),
    ('D', 'Painting'),
)


class VehicleComponent(models.Model):
    name = models.CharField(max_length=36)
    part_number = models.CharField(max_length=64, unique=True)
    quantity = models.IntegerField(default=1)

    # This is the time required to process or "integrate" this into the vehicle
    process_time = models.IntegerField(default=1)

    facility_required = models.CharField(choices=PRODUCTION_TYPE, max_length=16, default='A')

    def __str__(self):
        return self.name
