from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    #choices for role
    ROLE_CHOICES = [
        ('user','User'),
        ('admin','Admin'),
    ]

    address = models.CharField(max_length = 100)
    contact_number = models.CharField(max_length = 15)
    role = models.CharField(max_length = 10, choices = ROLE_CHOICES, default = 'user')


#model for book
class Book(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.SET_NULL, null = True, related_name = 'books')
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 50)
    price = models.PositiveIntegerField(default = 0)
    quantity = models.PositiveIntegerField(default = 0)


    def __str__(self):
        return str(f"{self.title} {self.author}")


#model for order
class Order(models.Model):
    
    #choices for order status
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed','Completed'),
        ('canceled','Canceled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'orders')
    book = models.ManyToManyField(Book,through = 'OrderItem')
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')

    def __str__(self):
        return str(f"{self.user}")


#model for order item
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'order_item')
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'book_order_item')
    quantity = models.PositiveIntegerField(default = 0)


#model for cart
class Cart(models.Model):

    #choices for cart status
    STATUS_CHOICES = [
        ('active','Active'),
        ('checked_out','Checked Out'),
        ('abandoned','Abandoned')
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = 'carts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'active')

    def __str__(self):
        return str(f"{self.user}")

#model for cart item
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE, related_name = 'cart_items')
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'book_items')
    quantity = models.PositiveIntegerField(default = 1)
