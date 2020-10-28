from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Url


# Create your views here.

def add_url(request):
    return render(request, '')


def fg(request, key):
    url = Url.objects.get(key=key)
    return HttpResponseRedirect(url.forward_url)
