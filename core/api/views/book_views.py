from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from core.api.serializers import book_serializers
from core.api.permissions.admin_permissions import isAdminUser
from core.models import Book

#Book views
class BookListView(APIView):

    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(responses = {status.HTTP_200_OK:book_serializers.BookSerializer()})
    def get(self,request):
        books = Book.objects.all()
        serializer = book_serializers.BookSerializer(books, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


#for ADMIN Book views
class BookCreateView(APIView):

    permission_classes = [IsAuthenticated,isAdminUser]

    @swagger_auto_schema(request_body = book_serializers.BookSerializer)
    def post(self,request):
        serializer = book_serializers.BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    permission_classes = [IsAuthenticated,isAdminUser]

    def get_object(self,book_id):
        try:
            return Book.objects.get(pk = book_id)
        except Book.DoesNotExist:
            raise NotFound(detail = 'Book not find')

    @swagger_auto_schema(responses = {status.HTTP_200_OK:book_serializers.BookSerializer()})
    def get(self,request,book_id):
        book = self.get_object(book_id)
        serializer = book_serializers.BookSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    @swagger_auto_schema(request_body = book_serializers.BookSerializer,responses = {status.HTTP_201_CREATED:book_serializers.BookSerializer()})
    def put(self,request,book_id):
        book = self.get_object(book_id)
        serializer = book_serializers.BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({
                "Message":"Edit Successfully",
                "Data":serializer.data
            },status = status.HTTP_201_CREATED)
        return Response({
            "Message":"Error",
            "Errors":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,book_id):
        book = self.get_object(book_id)
        book.delete()
        return Response({
            "Message":"Sucessfully deleted",
        },status = status.HTTP_204_NO_CONTENT)
