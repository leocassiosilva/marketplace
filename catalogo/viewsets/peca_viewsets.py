from catalogo.paginations.peca_pagination import StandardResultsSetPagination
from catalogo.serializers.peca_serializers import PecaSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Peca


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