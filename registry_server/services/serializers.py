from rest_framework import serializers

from .models import *

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('path',)

class ServiceSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True, read_only=True,)

    def create(self, validated_data):
        routes = validated_data.pop('routes')
        service, updated = Service.objects.update_or_create(**validated_data)
        for route in routes:
            route['service'] = service
            Route.objects.update_or_create(**route)
        return service

    class Meta:
        model = Service
        fields = (
            'name',
            'host',
            'port',
            'routes',
        )
