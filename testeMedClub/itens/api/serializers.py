from rest_framework import serializers
from itens import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.item
        fields =  '__all__'
        read_only_fields = ['id_item']