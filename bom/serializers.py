from rest_framework import serializers
from .models import Bom


class BomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bom
        fields = '__all__'
