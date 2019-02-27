from rest_framework import serializers
from .models import VehicleOrder


class VehicleOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleOrder
        fields = '__all__'
