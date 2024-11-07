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
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)


    def __str__(self):
        return str(f"{self.title} {self.author}")