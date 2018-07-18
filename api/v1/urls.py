from django.conf.urls import url, include
from .auth import urls as auth_urls
from django.urls import path

urlpatterns = [
    path('auth/', include('api.v1.auth.urls')),
    path('renewal/', include('api.v1.renewal.urls'))
]
