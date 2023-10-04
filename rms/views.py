from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import viewsets

from .models import *
from .serializers import *





# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    

    def destroy(self,request,pk):
        category=get_object_or_404(Category,pk=pk)

        food=Food.objects.filter(category=category)
        if food.count()>0:
            return Response({
                "detail":"You can't delete data Its is protect "
            })
        category.delete()
        return Response(
            {"detail":"Data has been deleted"}
            ,status=status.HTTP_204_NO_CONTENT
            )
    

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class=FoodSerializer
