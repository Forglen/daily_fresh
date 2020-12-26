from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from apps.goods import views

urlpatterns = [
    url(r'^$',views.index, name='index'),  # 首页
]
