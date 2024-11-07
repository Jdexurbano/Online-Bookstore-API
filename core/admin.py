from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('address','contact_number','role')}),)

    list_display = ('id','username','address','contact_number','role')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','quantity')

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Book,BookAdmin)