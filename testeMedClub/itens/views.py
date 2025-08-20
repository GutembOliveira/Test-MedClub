from rest_framework.decorators import action  # ✅
from django.shortcuts import render
from rest_framework import viewsets
from itens.api import serializers
from rest_framework.response import Response
from itens import models
from itens.models import item 

class ItemViewSet(viewsets.ModelViewSet):
    queryset = serializers.ItemSerializer.Meta.model.objects.all()
    serializer_class = serializers.ItemSerializer

    def perform_create(self, serializer):
        serializer.save()  # You can add custom logic here if needed

     # Rota GET /items/todos/
    @action(detail=False, methods=['get'])
    def todos(self, request):
        items = item.objects.all()  # pega todos os itens
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)