from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods, require_safe
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url, Stats


# Create your views here.

def add_url(request):
    url = request.GET.get('url')
    custom_key = request.GET.get('key')

    url_obj = Url.objects.create(
        forward_url=url,
        custom_key=custom_key
    )

    data = {
        'url': f'{ request.scheme }://{ request.get_host() }{ url_obj.compose_url }'
    }

    return JsonResponse(
        status=status.HTTP_200_OK,
        data=data,
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


class StatsList(APIView):
    permission_classes = [IsAuthenticated, ]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/stats.html'

    def get(self, request):
        queryset = Url.objects.annotate(number_of_visitors=Count('stats__visitor'))
        return Response(
            {
                'urls': queryset
            }
        )


def main_view(request):
    return render(request, 'main/main.html')
