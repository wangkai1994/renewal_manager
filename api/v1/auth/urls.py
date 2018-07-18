from django.conf.urls import url, include
from rest_framework import routers

from django.urls import path
from . import views
from rest_framework_jwt.views import verify_jwt_token
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('permissions', views.PermissionViewSet)
router.register('userobjectpermissions', views.UserObjectPermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_jwt_token),
    path('token/refresh/', views.refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('register/', views.register),
    path('login/', views.login),
    path('test/', views.test),
]
