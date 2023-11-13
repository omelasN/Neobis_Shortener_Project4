from django.db import models
 

class UrlShortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15)

    def __str__(self):
        return self.long_url
