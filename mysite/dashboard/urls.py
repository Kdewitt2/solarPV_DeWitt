from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dash', views.IndexView.as_view(), name='dash'),
]