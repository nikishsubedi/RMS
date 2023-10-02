from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import viewsets
# from rest_framework import generics


from .models import *
from .serializers import *



# using viewsets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# using generics
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer



# class CategoryList(APIView):
#     def get(self,request):
#         categories= Category.objects.all()
#         serializer=CategorySerializer(categories,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#             )
        
    
        

# class CategoryDetail(APIView):
#     def get(self,request,pk):
#         categories = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializer(categories,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def patch(self,request,pk):
#         category = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializer(category,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )
    
#     def delete(self,request,pk):
#         category = get_object_or_404(Category,pk=pk)
#         food = Food.objects.filter(category=category)
#         if food.count() > 0:
#             return Response({
#                 "detail":"You can't delete data. It is protected"
#             })
#         category.delete()
#         return Response(
#             {"detail": "Data deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )
        

    