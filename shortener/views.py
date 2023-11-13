from django.shortcuts import render
from rest_framework import generics
from .models import UrlShortener
from .serializers import ShortenerSerializer


class UrlShortenerView(generics.CreateAPIView):
    queryset = UrlShortener.objects.all()
    serializer_class = ShortenerSerializer
