from django.urls import path
from . import views

urlpatterns = [
    path('s/<key>', views.get_url, name='get_url'),
    path('add', views.add_url, name='add_url'),
    path('stats/', views.StatsList.as_view(), name='stats'),
    path('', views.main_view, name='main')
]
