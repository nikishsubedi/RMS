from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields=("id","name",)
       
class FoodSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source = "category"
    )
    category = CategorySerializer()
    price_tax = serializers.SerializerMethodField("price_with_tax")
    
    def price_with_tax(self,food):
        return round((float(food.price)*1.13),2)
        
    class Meta:
        model = Food
        fields = (
            "id",
            "name",
            "price",
            "price_tax",
            "category",
            "category_id",
                  )
