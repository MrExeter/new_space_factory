from rest_framework import serializers
from .models import VehicleComponent


class VehicleComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleComponent
        fields = '__all__'
