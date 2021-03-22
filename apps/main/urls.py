from django.urls import path
from . import views

urlpatterns = [
    path('s/<key>', views.get_url, name='get_url'),
    path('add', views.add_url, name='add_url'),
    path('', views.main_view, name='main')
]
