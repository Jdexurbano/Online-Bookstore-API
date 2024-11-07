from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('address','contact_number','role')}),)

    list_display = ('id','username','address','contact_number','role')

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)