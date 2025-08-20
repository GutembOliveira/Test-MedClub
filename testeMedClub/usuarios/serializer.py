from rest_framework import serializers
from usuarios.models import usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = [ 'nome', 'email', 'senha']  
        extra_kwargs = {
            'senha': {'write_only': True} 
        }

class LoginSerializer(serializers.Serializer):
    nome = serializers.CharField()
    senha = serializers.CharField(write_only=True)