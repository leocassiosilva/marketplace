from django.urls import include, path
from rest_framework import routers
from core.viewsets.user_viewsets import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path("", include(user_router.urls)),
]