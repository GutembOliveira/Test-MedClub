from rest_framework import serializers
from usuarios.models import Usuario
from rest_framework.exceptions import PermissionDenied

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "senha", "is_admin"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        senha = validated_data.pop("senha")
        is_admin_request = validated_data.get("is_admin", False)

        request = self.context.get("request")
        existe_admin = Usuario.objects.filter(is_admin=True).exists()

        if is_admin_request and existe_admin:
            if not (request and getattr(request.user, "is_authenticated", False) and getattr(request.user, "is_admin", False)):
                raise PermissionDenied("Somente um usuário admin pode criar outro admin.")

        user = Usuario(**validated_data)
        user.set_password(senha)  # grava o hash em 'password'
        user.save()
        return user
