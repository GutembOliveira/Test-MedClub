from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from usuarios.models import Usuario
from .serializer import UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.hashers import check_password

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        # Permite usar o create do serializer que já faz validação de admin
        serializer.save()

    @action(detail=False, methods=['get'])
    def todos(self, request):
        user = request.user
        usuarios = Usuario.objects.all()  # pega todos os itens
        serializer = self.get_serializer(usuarios, many=True)
        return Response(serializer.data)

class LoginView(APIView):
    permission_classes = []  # libera o login sem autenticação

    def post(self, request):
        email = request.data.get("email")
        senha = request.data.get("senha")

        if not email or not senha:
            return Response({"erro": "Email e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(senha):
            return Response({"erro": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
