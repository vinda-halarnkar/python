from rest_framework import serializers
from .models import List, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'completed', 'color']  # Adjust fields as needed

class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)  # Add the related items using nested serializer

    class Meta:
        model = List
        fields = ['name', 'items']