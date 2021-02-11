from django.urls import include, path

from overview.views import overview

urlpatterns = [
    path('', overview),
]