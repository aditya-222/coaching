from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'institutes', views.institutes, name='institutes'),
]