from django.urls import path, path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
router = DefaultRouter()
router.register(r'', TodoViewSet, basename='todo')
urlpatterns = [

]+router.urls
