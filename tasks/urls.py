from django.urls import include, path

# Temporary responce stub
from django.shortcuts import HttpResponse

urlpatterns = [
    path('', HttpResponse),
]