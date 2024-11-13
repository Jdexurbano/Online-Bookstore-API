from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import order_item_serializers
from core.models import CustomUser,Order
from core.api.permissions.admin_permissions import isAdminUser

class OrderItemList(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses = {status.HTTP_200_OK:order_item_serializers.OrderSerializer()})
    def get(self,request):
        user = CustomUser.objects.get(username = request.user)
        orders = user.orders.all()
        serializer = order_item_serializers.OrderSerializer(orders, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @swagger_auto_schema(request_body = order_item_serializers.OrderItemSerializer)
    def post(self,request):
        serializer = order_item_serializers.OrderItemSerializer(data = request.data, context = {'user':request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({"Message":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


class OrderItemDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self,order_id):
        try:
            return Order.objects.get(pk = order_id)
        except Order.DoesNotExist:
            raise NotFound(detail = 'Order not found')

    @swagger_auto_schema(responses = {status.HTTP_200_OK:order_item_serializers.OrderSerializer()})
    def get(self,request,order_id):
        order = self.get_object(order_id)
        serializer = order_item_serializers.OrderSerializer(order)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body = order_item_serializers.UpdateOrderStatusSerializer, responses = {status.HTTP_201_CREATED:order_item_serializers.UpdateOrderStatusSerializer()})
    def patch(self,request,order_id):
        order = self.get_object(order_id)
        serializer = order_item_serializers.UpdateOrderStatusSerializer(order, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({
            "Message":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)


#FOR ADMIN VIEWS
class OrderListForAdminView(APIView):

    permission_classes = [IsAuthenticated,isAdminUser]

    @swagger_auto_schema(responses = {status.HTTP_200_OK:order_item_serializers.OrderSerializer()})
    def get(self,request):
        orders = Order.objects.order_by('user')
        serializer = order_item_serializers.OrderSerializer(orders, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class OrderDetailForAdminView(APIView):

    permission_classes = [IsAuthenticated,isAdminUser]

    def get_object(self,order_id):
        try:
            return Order.objects.get(pk = order_id)
        except Order.DoesNotExist:
            raise NotFound(detail = 'Order not found')
    
    @swagger_auto_schema(responses = {status.HTTP_200_OK:order_item_serializers.OrderSerializer()})
    def get(self,request,order_id):
        order = self.get_object(order_id)
        serializer = order_item_serializers.OrderSerializer(order)
        return Response(serializer.data, status = status.HTTP_200_OK)
