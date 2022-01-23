from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.main.models import Url


class UrlSerializer(ModelSerializer):
    compose_url = ReadOnlyField(source='compose_url')

    class Meta:
        model = Url
        fields = ('compose_url',)
