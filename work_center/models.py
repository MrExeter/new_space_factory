from django.db import models


class WorkCenter(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
