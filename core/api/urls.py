from django.urls import path, include
from core.api.views import user_views,book_views, order_item_views
from rest_framework_simplejwt.views import(TokenRefreshView,TokenObtainPairView)


urlpatterns = [

    #authentication
    path('token/',TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),

    #register
    path('register/',user_views.UserRegistrationView.as_view(),name='register'),

    #user detail
    path('user/',user_views.UserDetailView.as_view(),name = 'user_detail'),

    #book
    path('books/',book_views.BookListView.as_view(),name = 'book_list'),
    path('books/create/',book_views.BookCreateView.as_view(), name = 'book_create'),
    path('books/<int:book_id>/',book_views.BookDetailView.as_view(), name = 'book_detail'),

    #order item
    path('orders/',order_item_views.OrderItemList.as_view(),name = 'order_item_list'),
    path('orders/<int:order_id>/',order_item_views.OrderItemDetailView.as_view(), name = 'order_detail'),
]