from django.contrib import admin

# Register your models here.
from apps.main.models import Url, Stats, Visitor

admin.site.register([Url, Stats, Visitor])
