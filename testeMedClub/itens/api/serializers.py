from rest_framework import serializers
from itens import models


class ItemSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=100)
    preco = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    error_messages={
        'invalid': 'O preço deve ser um número válido.',
        'max_digits': 'O preço excede o limite de dígitos permitido.',
    }
    )
    
    class Meta:
        model = models.item
        fields =  '__all__'
        read_only_fields = ['id_item']