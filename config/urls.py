from django.contrib import admin
from django.urls import path, include
from shortener.views import Redirector

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("shortener.urls")),
    path("shortener/", include("shortener.urls")),
    path("redirect<str:short_url>/", Redirector.as_view(), name="redirect-url"),

]
