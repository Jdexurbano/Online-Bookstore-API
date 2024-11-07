from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import user_serializer
from core.models import CustomUser

#User Registration
class UserRegistrationView(APIView):

    @swagger_auto_schema(request_body = user_serializer.UserRegistrationSerializer, responses = {status.HTTP_201_CREATED:user_serializer.UserRegistrationSerializer()})
    def post(self,request):
        serializer = user_serializer.UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({
            "Message":"Validation Error",
            "Error":serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)


#User detail
class UserDetailView(APIView):

    @swagger_auto_schema(responses = {status.HTTP_200_OK:user_serializer.UserSerializer()})
    def get(self,request):
        user = CustomUser.objects.get(username = request.user)
        serializer = user_serializer.UserSerializer(user)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body = user_serializer.UserSerializer,responses = {status.HTTP_201_CREATED:user_serializer.UserSerializer()})
    def put(self,request):
        user = CustomUser.objects.get(username = request.user)
        serializer = user_serializer.UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({
                "Message":"Edit Successfully",
                "Data":serializer.data
            },status = status.HTTP_201_CREATED)
        return Response({
            "Message":"Error",
            "Error":serializer.errors
        })
    
    def delete(self,request):
        user = CustomUser.objects.get(username = request.user)
        user.delete()
        return Response({"Message":"Accoun successfully delete"},status = status.HTTP_204_NO_CONTENT)