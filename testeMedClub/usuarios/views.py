from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from usuarios.serializer import LoginSerializer, UsuarioSerializer
from usuarios.models import usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        senha = make_password(serializer.validated_data['senha'])
        serializer.validated_data['senha'] = senha
        serializer.save(senha=senha)  # Save the hashed password


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nome = serializer.validated_data['nome']
        senha = serializer.validated_data['senha']
        try:
            user = usuario.objects.get(nome=nome)
        except usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=404)


        if check_password(senha, usuario.nome):
            return Response({"mensagem": "Login bem-sucedido"})
        else:
            return Response({"erro": "Senha incorreta"}, status=401)