from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'Online book store API',
        default_version = 'v1',
        description = 'API for online Book store',
        contact = openapi.Contact(email = 'dexterurbano25@gmail.com'),
    ),

    public = True,
    permission_classes = (permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('core.api.urls'),name='api'),

    #swagger documentation URL
    path('swagger/',schema_view.with_ui('swagger',cache_timeout = 0),name = 'schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout = 0), name = 'schema-redoc'),
]
