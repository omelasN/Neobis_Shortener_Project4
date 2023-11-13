from django.shortcuts import render, redirect
from rest_framework import generics
from django.http import HttpResponse

from .models import UrlShortener
from .serializers import ShortenerSerializer
from django.views import View
from django.conf import settings


class ShortenerView(generics.ListAPIView):
    queryset = UrlShortener.objects.all()
    serializer_class = ShortenerSerializer


class ShortenerCreateView(generics.CreateAPIView):
    serializer_class = ShortenerSerializer


class ExpandShortUrlView(generics.RetrieveAPIView):
    queryset = UrlShortener.objects.all()
    serializer_class = ShortenerSerializer
    lookup_url_kwarg = 'short_url'


class Redirector(View):
    def get(self, request, short_url, *args, **kwargs):
        redirect_url = UrlShortener.objects.filter(short_url=settings.HOST_URL + "/" + short_url).first()
        if redirect_url:
            return redirect(redirect_url.long_url)
        else:
            return HttpResponse("Error")


