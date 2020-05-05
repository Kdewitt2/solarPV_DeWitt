from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'clientForm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('productForm', views.IndexView.as_view(), name='productForm'),
]