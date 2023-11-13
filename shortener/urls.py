from django.urls import path
from .views import UrlShortenerView


urlpatterns = [
    path("shortener/", UrlShortenerView.as_view(), name="longurl"),

]