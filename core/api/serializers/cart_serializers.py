from rest_framework import serializers
from core.api.serializers import cart_item_serializers
from core.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user','status']

class CartStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['status']