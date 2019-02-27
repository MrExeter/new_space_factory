from rest_framework import serializers
from .models import WorkCenter


class WorkCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkCenter
        fields = '__all__'
