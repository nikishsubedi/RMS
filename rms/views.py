from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import viewsets
from django_filters import rest_framework as filter
from .models import *
from .serializers import *
from .filters import *
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS





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
    queryset = Food.objects.select_related('category').all()
    serializer_class=FoodSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = FoodFilter
    search_fields = ('name',)


class TableViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    #serializer_class = TableSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('number','is_occupied',)

    def get_serializer_class(self):

        if self.request.method is SAFE_METHODS:
            return TableSerializer
        return CreateUpdateTableSerializer