from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'locationForm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('locationForm', views.IndexView.as_view(), name='locationForm'),
]