from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from apps.user import views

urlpatterns = [
    url(r'register$', views.register, name='register'),
    url(r'register_handle', views.register_handle, name='register_handle')
]
