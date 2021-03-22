from django.db import models
import uuid

# Create your models here.


class Url(models.Model):
    """
    Url shortener main model.

    ej: https://www.boring-link.com/sdkflhasdokfhasdfk&ASDF=3?ADF=3   -> s.noheaven.net/LC3J

    """
    key = models.CharField(max_length=8)
    forward_url = models.URLField()

    def save(self, *args, **kwargs):
        self.key = uuid.uuid4().__str__()[:4]
        super().save()

    def __str__(self):
        return f'Key: {self.key} - Url: {self.forward_url}'
