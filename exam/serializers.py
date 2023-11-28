from rest_framework import serializers
from .models import * 


class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField(allow_null=True)
    customer = serializers.IntegerField(allow_null=True)
    doctor = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return Appointment(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
