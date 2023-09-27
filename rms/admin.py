from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','total',)
    search_fields = ('name',)
    list_per_page=10
    ordering = ('id','name')
    def total(self,category):
        return models.Food.objects.filter(category=category).count()
    
@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "price",
        "taxed_price",
        "category",
    )
    search_fields=('name','category')
    autocomplete_fields=('category',)
    list_filter=('category',)
    list_per_page=10
    list_select_related=('category',)
    
    def taxed_price(self,food):
        return float(food.price)+float(food.price)*0.13
    
admin.site.register(models.Table)
admin.site.register(models.Profile)

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=(
        'food',
        'order',
    )
    search_fields=('food','order',)
    autocomplete_fields=('food',)

class OrderItemInline(admin.StackedInline):
    model=models.OrderItem

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'table',
        'user',
        'payment_status',
        'status',
    )
    

    inlines=(OrderItemInline,)

admin.site.register(models.OrderItem)