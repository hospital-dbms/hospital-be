from rest_framework import serializers
from .models import * 


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(allow_null=False)
    is_staff = serializers.BooleanField(allow_null=False)

    def create(self, validated_data):
        return UserModel(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
