from rest_framework import viewsets

from .models import WorkCenter
from .serializers import WorkCenterSerializer


class WorkCenterView(viewsets.ModelViewSet):
    queryset = WorkCenter.objects.all()
    serializer_class = WorkCenterSerializer
