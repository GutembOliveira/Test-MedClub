from django.shortcuts import render
from rest_framework import viewsets
from itens.api import serializers
from itens import models 

class ItemViewSet(viewsets.ModelViewSet):
    queryset = serializers.ItemSerializer.Meta.model.objects.all()
    serializer_class = serializers.ItemSerializer

    def perform_create(self, serializer):
        serializer.save()  # You can add custom logic here if needed