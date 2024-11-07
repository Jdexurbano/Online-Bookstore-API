from django.urls import path, include
from core.api.views import user_views
from rest_framework_simplejwt.views import(TokenRefreshView,TokenObtainPairView)


urlpatterns = [

    #authentication
    path('token/',TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),

    #register
    path('register/',user_views.UserRegistrationView.as_view(),name='register'),
]