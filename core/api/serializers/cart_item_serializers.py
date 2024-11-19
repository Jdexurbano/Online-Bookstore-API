from rest_framework import serializers
from core.models import Cart,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','cart_id','book','quantity']
    
    
    def create(self, validated_data):

        cart = Cart.objects.get(user = self.context['user'])

        cart_item = CartItem.objects.create(
            cart = cart,
            book = validated_data['book'],
            quantity = validated_data['quantity']
        )

        cart_item.save()
        return cart_item