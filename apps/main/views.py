from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Url


# Create your views here.

def add_url(request):
    url = request.GET.get('url')
    url_obj = Url.objects.create(
        forward_url=url
    )

    return JsonResponse(
        {
            'code': 200,
            'url': 'http://' + request.get_host() + reverse_lazy('get_url').__str__() + url_obj.key
        }
    )


def get_url(request, key):
    print(2)

    url = Url.objects.filter(key=key)

    if url.exists():
        return HttpResponseRedirect(url.forward_url)
    return render(request, 'main/main.html')


def main_view(request):
    print(1)
    return render(request, 'main/main.html')
