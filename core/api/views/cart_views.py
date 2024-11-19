from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import cart_serializers
from core.models import Cart

class CartList(APIView):
    permission_classes = [IsAuthenticated]

    def check_if_cart_exist(self):
        try:
            return Cart.objects.get(user = self.request.user)
        except Cart.DoesNotExist:
            raise NotFound(detail = 'No cart exists for this user.')

    @swagger_auto_schema(responses = {status.HTTP_200_OK:cart_serializers.CartSerializer()})
    def get(self,request):
        cart = self.check_if_cart_exist()
        serializer = cart_serializers.CartSerializer(cart)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @swagger_auto_schema(request_body = cart_serializers.CartSerializer)
    def post(self,request):
        serialzer = cart_serializers.CartSerializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status = status.HTTP_201_CREATED)
        return Response({
            "Message":serialzer.errors
        },status = status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body = cart_serializers.CartStatusSerializer)
    def patch(self,request):
        cart = self.check_if_cart_exist()
        serializer = cart_serializers.CartStatusSerializer(cart,data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({
            "Message":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)