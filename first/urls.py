from django.contrib import admin
from . import views
from django.urls import include, path


urlpatterns = [
    path('', views.my_first),
]