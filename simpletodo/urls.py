"""Root URLConf module."""

from django.contrib import admin
from django.urls import include, path

from simpletodo.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('overview/', include('overview.urls')),
    path('tags/', include('tags.urls')),
]
