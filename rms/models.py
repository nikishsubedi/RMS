from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    

class Food(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name="foods")
    
    def __str__(self) -> str:
        return self.name
    
class Table(models.Model):
    number=models.IntegerField()
    is_occupied=models.BooleanField(default=False)
    
class Profile(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    
    GENDER_CHOICES=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'FEMALE'),
    ]
    phone_number=models.CharField(max_length=10)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    
    
class Order(models.Model):
    PENDING_STATUS='P'
    COOKING_STATUS='CO'
    CANCELLED_STATUS='CA'
    COMPLETED_STATUS='C'
    
    ORDER_STATUS=[
        (PENDING_STATUS,'PENDING'),
        (COOKING_STATUS,'COOKING'),
        (CANCELLED_STATUS,'CANCELLED'),
        (COMPLETED_STATUS,'COMPLETED'),
        
    ]
    
    
    table=models.ForeignKey(Table,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    payment_status=models.BooleanField(default=False)
    status=models.CharField(choices=ORDER_STATUS,max_length=2,default=PENDING_STATUS)
    

class OrderItem(models.Model):
    food=models.ForeignKey(Food,on_delete=models.PROTECT)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)