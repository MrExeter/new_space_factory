from rest_framework import viewsets

from .models import Bom
from .serializers import BomSerializer


class BomView(viewsets.ModelViewSet):
    queryset = Bom.objects.all()
    serializer_class = BomSerializer
