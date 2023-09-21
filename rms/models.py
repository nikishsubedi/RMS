from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    
class Table(models.Model):
    number=models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    
class Profile(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    GENDER_CHOICES = [
        (MALE_CHOICE, 'Male'),
        (FEMALE_CHOICE, 'Female'),
        (OTHER_CHOICE, 'Other'),
    ]
    phone_number=models.CharField(max_length=10)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Order(models.Model):
    
    PENDING_STATUS='P'
    COOKING_STATUS='CO'
    COMPLETED_STATUS='C'
    CANCELLED_STATUS='CA' 
    
    ORDER_STATUS = [
        (PENDING_STATUS, 'Pending'),
        (COOKING_STATUS, 'Cooking'),
        (COMPLETED_STATUS, 'Completed'),
        (CANCELLED_STATUS, 'Cancelled'),
        
    ]
    
    table=models.ForeignKey(Table,on_delete=models.PROTECT)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    payment_status=models.BooleanField(default=False)
    status = models.CharField(choices=ORDER_STATUS,max_length=2,default=PENDING_STATUS)