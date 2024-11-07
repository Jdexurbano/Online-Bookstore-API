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

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}")
    