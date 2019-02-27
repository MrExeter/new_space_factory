from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
