import uuid
from django.db import models
from usuarios.models import Usuario
from itens.models import item  # app de itens


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="pedidos")
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_valor(self):
        total = sum([pi.item.preco * pi.quantidade for pi in self.itens.all()])
        self.valor = total
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.nome} (R$ {self.valor})"


class PedidoItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.item.nome}"
