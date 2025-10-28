from django.urls import include, path
from catalogo.viewsets.peca_viewsets import PecaViewSet
from rest_framework import routers

peca_router = routers.DefaultRouter()
peca_router.register(r'peca', PecaViewSet, basename='peca')




urlpatterns = [
    path("", include(peca_router.urls)),
]