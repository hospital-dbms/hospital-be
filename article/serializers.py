from rest_framework import serializers
from .models import * 


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=False)
    title = serializers.CharField()
    tag = serializers.CharField(allow_null=True)
    content = serializers.CharField(allow_null=True)
  
    def create(self, validated_data):
        return Article(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
