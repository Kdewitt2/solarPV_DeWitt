from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'testStandardForm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('testStandardForm', views.IndexView.as_view(), name='testStandardForm'),
]