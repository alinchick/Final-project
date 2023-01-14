from urllib import request

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('vostr', views.vostr),
    path('geo', views.geo),
    path('skills', views.skills)
]
