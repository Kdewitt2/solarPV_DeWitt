from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'certificateForm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('certificateForm', views.IndexView.as_view(), name='certificateForm'),
]