from django.urls import include, path
from catalogo.viewsets.peca_viewsets import PecaViewSet
from rest_framework import routers

post_router = routers.DefaultRouter()
post_router.register(r'peca', PecaViewSet, basename='peca')




urlpatterns = [
    path("", include(post_router.urls)),
]