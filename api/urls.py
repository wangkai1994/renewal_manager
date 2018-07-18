from django.conf.urls import url, include
from .v1 import urls as v1_urls
from django.urls import path

urlpatterns = [
    path('', include(v1_urls)),  # default is the latest
    path('v1/', include(v1_urls)),
]
