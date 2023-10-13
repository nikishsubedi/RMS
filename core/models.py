from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_ADMIN = 'A'
    USER_CASHIER = 'C'
    USER_CHEF = 'CH'
    USER_WAITER = 'W'
    
    USER_TYPES = [
        (USER_ADMIN, 'ADMIN'),
        (USER_CASHIER, 'CASHIER'),
        (USER_WAITER, 'WAITER'),
        (USER_CHEF,'CHEF'),
    ]
    type = models.CharField(choices=USER_TYPES, max_length=2,)
    phone_number = models.CharField(max_length=50,null=True)

    def isAdmin(self):
        return self.type == 'Admin'
