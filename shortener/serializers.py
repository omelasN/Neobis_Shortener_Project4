from rest_framework import serializers
from .models import UrlShortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = ["long_url"]
