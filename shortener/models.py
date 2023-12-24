from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings
 

class UrlShortener(models.Model):
    objects = None
    long_url = models.URLField(unique=True)
    short_url = models.URLField(blank=True, null=True, unique=True)

 def shortener(self):
    while True:
        random_string = "".join(choices(ascii_letters, k=6))
        new_url = settings.HOST_URL+"/"+random_string
        if not UrlShortener.objects.filter(short_url=new_url).exists():
            break
    return new_url
def save(self,*args,**kwargs):
    if not self.short_url:
        new_url = self.shortener()
        self.short_url = new_url
    return super().save(*args, **kwargs)
