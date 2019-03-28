from django.db import models

PRODUCTION_TYPE = (
    ('A', 'Assembly'),
    ('B', 'Electronics'),
    ('C', 'Machining'),
    ('D', 'Painting'),
)


class WorkCenter(models.Model):
    """Represents a work center that processes components"""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    is_available = models.BooleanField(default=True)

    # This is the type of work-center
    production_type = models.CharField(choices=PRODUCTION_TYPE, max_length=16, default='A')

    def __str__(self):
        return self.name
