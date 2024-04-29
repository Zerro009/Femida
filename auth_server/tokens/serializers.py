from rest_framework import serializers

from .models import *

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'access_token',
            'refresh_token',
        )
