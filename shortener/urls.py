from django.urls import path
from .views import ShortenerView, ShortenerCreateView, ExpandShortUrlView


urlpatterns = [
    path("", ShortenerView.as_view(), name="short-url"),
    path("create/", ShortenerCreateView.as_view(), name="create-url"),
    path("expand/<str:short_url>/", ExpandShortUrlView.as_view(), name="expand-url"),


]