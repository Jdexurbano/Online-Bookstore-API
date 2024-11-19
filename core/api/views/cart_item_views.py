from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import cart_item_serializers
from core.models import CartItem,Cart


class CartItemList(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses = {status.HTTP_200_OK:cart_item_serializers.CartItemSerializer()})
    def get(self,request):
        cart = Cart.objects.get(user = request.user)
        cart_items = cart.cart_items.all()
        serializer = cart_item_serializers.CartItemSerializer(cart_items, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @swagger_auto_schema(request_body = cart_item_serializers.CartItemSerializer)
    def post(self,request):
        serializer = cart_item_serializers.CartItemSerializer(data = request.data, context = {'user':request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({
            "Message":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)

class CartItemDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self,item_id):
        try:
            cart = Cart.objects.get(user = self.request.user)
            return cart.cart_items.get(pk = item_id)
        except CartItem.DoesNotExist:
            raise NotFound(detail = 'No item exist')
    
    @swagger_auto_schema(responses = {status.HTTP_200_OK:cart_item_serializers.CartItemSerializer()})
    def get(self,request,item_id):
        cart_item = self.get_object(item_id)
        serializer = cart_item_serializers.CartItemSerializer(cart_item)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body = cart_item_serializers.CartItemSerializer)
    def put(self,request,item_id):
        cart_item = self.get_object(item_id)
        serializer = cart_item_serializers.CartItemSerializer(cart_item,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({
            "Message":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)


    def delete(self,request,item_id):
        cart_item = self.get_object(item_id)
        cart_item.delete()
        return Response({
            "Message":'Item delete'
        },status = status.HTTP_204_NO_CONTENT)