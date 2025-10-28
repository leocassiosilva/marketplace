from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from core.serializers.user_serializers import RegisterSerializer, UserUpdateSerializer



class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    # Apenas create e update
    http_method_names = ['post', 'put', 'patch']

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return UserUpdateSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    # Criar usuário
    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserUpdateSerializer(user).data, status=status.HTTP_201_CREATED)

    # Atualizar usuário logado
    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
