from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Url, Stats


# Create your views here.

def add_url(request):
    url = request.GET.get('url')
    custom_key = request.GET.get('key')

    url_obj = Url.objects.create(
        forward_url=url,
        custom_key=custom_key
    )

    final_key = url_obj.key or url_obj.custom_key

    return JsonResponse(
        {
            'code': 200,
            'url': 'https://' + request.get_host() + str(reverse_lazy('get_url', args=[final_key]))
        }
    )


def get_url(request, key):
    query = Q(key=key) | Q(custom_key=key)
    url = Url.objects.filter(query)

    if url.exists():
        url = url.first()
        stats = Stats.objects.get(url=url)
        stats.add_visitor(request.environ.get('REMOTE_ADDR'))

        return HttpResponseRedirect(url.forward_url)

    return render(request, 'main/main.html')


def main_view(request):
    return render(request, 'main/main.html')
