import datetime

from django.db import models
import uuid

from django.db.models import CASCADE


class Url(models.Model):
    """
    Url shortener main model.

    ej: https://www.boring-link.com/sdkflhasdokfhasdfk&ASDF=3?ADF=3   -> s.noheaven.net/LC3J

    """
    key = models.CharField(max_length=8, null=True)
    forward_url = models.URLField()
    custom_key = models.CharField(max_length=8, null=True)

    def save(self, *args, **kwargs):
        if not self.custom_key:
            self.key = uuid.uuid4().__str__()[:4]

        super().save()
        Stats.objects.create(url=self)

    def __str__(self):
        return f'Key: {self.key} Custom Key: {self.custom_key} - Url: {self.forward_url}'


class Stats(models.Model):
    url = models.ForeignKey(Url, on_delete=CASCADE)
    times_clicked = models.IntegerField(default=0)

    def add_visitor(self, ip_address):
        Visitor.objects.create(stats=self, visited_on=datetime.datetime.now(), ip_address=ip_address)

    def __str__(self):
        return f'Url {self.url} - times_clicked {self.times_clicked}'


class Visitor(models.Model):
    stats = models.ForeignKey(Stats, on_delete=CASCADE)
    visited_on = models.DateTimeField()
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'Stats {self.stats} - Visited on {self.visited_on} - ip address {self.ip_address}'
