from django.db import models


# Create your models here.


class Url(models.Model):
    """
    Url shortener main model.

    ej: https://www.boring-link.com/sdkflhasdokfhasdfk&ASDF=3?ADF=3   -> s.noheaven.net/LC3J

    """
    key = models.CharField(null=False, max_length=8)
    forward_url = models.URLField()

    def __str__(self):
        return f'Key: {self.key} - Url: {self.forward_url}'
