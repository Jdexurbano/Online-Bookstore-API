from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import user_serializer

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