"""
Created by Allen on '2018/11/21 12:42'
"""
__author__ = 'Allen'
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^show/$', views.show),
]
