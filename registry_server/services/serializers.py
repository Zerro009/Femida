from rest_framework import serializers

from .models import *

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('path',)

class ServiceSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True, read_only=True,)

    def create(self, validated_data):
        service, updated = Service.objects.update_or_create(**validated_data)
        return service

    class Meta:
        model = Service
        fields = (
            'name',
            'host',
            'port',
            'routes',
        )
