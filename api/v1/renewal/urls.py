from django.conf.urls import url, include
from rest_framework import routers

from django.urls import path
from . import views
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register('project', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
