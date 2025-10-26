from catalogo.paginations.peca_pagination import StandardResultsSetPagination
from catalogo.serializers.peca_serializers import PecaSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS

from ..models import Peca
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'head', 'options']
    
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    pagination_class = StandardResultsSetPagination
    search_fields = [
        'nome', 
        'descricao', 
    ]
    ordering_fields = [
        'nome', 
        'preco',
        'id'
    ]
    
    def get_permissions(self):
        """
        Retorna permissões dependendo do método HTTP.
        - Métodos seguros (GET, HEAD, OPTIONS) -> AllowAny
        """
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]


    @method_decorator(cache_page(60 * 15, key_prefix="pecas_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        import time 
        time.sleep(2) 
        return super().get_queryset()
    