from core.models import OrderItem,CustomUser,Book, Order
from rest_framework import serializers
from core.api.serializers import book_serializers, user_serializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','book','quantity']
    
    def create(self, validated_data):
       #create an order
        order = Order.objects.create(user = self.context['user'])

        #create the order item
        order_item = OrderItem.objects.create(
            order = order,
            book = validated_data['book'],
            quantity = validated_data['quantity']
        )

        #update the quantiy of the book if someone order
        book = validated_data['book']
        book.quantity -= validated_data['quantity']
        book.save()

        return order_item

class OrderSerializer(serializers.ModelSerializer):
    book = book_serializers.BookSerializer(many = True)
    user = user_serializer.UserSerializer()
    class Meta:
        model = Order
        fields = ['id','status','user','book']


class UpdateOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','status']