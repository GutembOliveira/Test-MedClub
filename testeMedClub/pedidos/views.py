from rest_framework import viewsets, permissions
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.decorators import action  
from rest_framework.response import Response


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)



    @action(detail=False, methods=['get'])
    def todos(self, request):
        pedidos = self.get_queryset()
        serializer = self.get_serializer(pedidos, many=True)
        return Response(serializer.data)