from rest_framework import viewsets

from .models import VehicleComponent
from .serializers import VehicleComponentSerializer


class VehicleComponentView(viewsets.ModelViewSet):
    queryset = VehicleComponent.objects.all()
    serializer_class = VehicleComponentSerializer
