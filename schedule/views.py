from rest_framework import viewsets

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
