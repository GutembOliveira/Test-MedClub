from rest_framework import serializers
from .models import Pedido, PedidoItem
from itens.models import item


class PedidoItemSerializer(serializers.ModelSerializer):
    item_id = serializers.UUIDField(write_only=True)
    item_nome = serializers.CharField(source="item.nome", read_only=True)
    item_preco = serializers.DecimalField(source="item.preco", max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = PedidoItem
        fields = ["item_id", "item_id", "item_nome", "item_preco", "quantidade"]


class PedidoSerializer(serializers.ModelSerializer):
    itens = PedidoItemSerializer(many=True)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Pedido
        fields = ["id", "usuario", "valor", "itens"]
        read_only_fields = ["usuario", "valor"]

    def create(self, validated_data):
        pedidoItens = validated_data.pop("itens")
        usuario = self.context["request"].user
        pedido = Pedido.objects.create(usuario=usuario)
        total = 0
        for item_data in pedidoItens:
            item_obj = item.objects.get(id_item=item_data["item_id"])
            PedidoItem.objects.create(
                pedido=pedido,
                item_id=item_data["item_id"],
                quantidade=item_data["quantidade"]
            )
            total += item_obj.preco * item_data["quantidade"]
        pedido.valor = total
        pedido.save()
        return pedido

    