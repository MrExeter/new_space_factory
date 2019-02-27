from rest_framework import viewsets

from .models import VehicleOrder
from .serializers import VehicleOrderSerializer


class VehicleOrderView(viewsets.ModelViewSet):
    queryset = VehicleOrder.objects.all()
    serializer_class = VehicleOrderSerializer

