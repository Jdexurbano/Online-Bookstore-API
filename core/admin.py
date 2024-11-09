from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Order,OrderItem

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('address','contact_number','role')}),)

    list_display = ('id','username','address','contact_number','role')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order','book','quantity')

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)