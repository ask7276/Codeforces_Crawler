from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.cf_home, name='cf_home'),
    # url(r'data/', views.data, name='chat'),
    url(r'^(?P<name>[\w\-\.\@]+)/$', views.analysis, name='analysis'),
]
