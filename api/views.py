from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Dishes, Ingredients
from .serializers import DishesSerializer, CategoryDishSerializer, IngredientsSerializer, CategorySerializer, ItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

class CatDishView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDishSerializer

class RetreiveCatDishView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDishSerializer
    lookup_field = 'title'

class DishView(generics.ListAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

class RetreiveDishView(generics.RetrieveDestroyAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

class singleDishView(APIView):
    def get(self, request, name=None, format=None):
        name = name
        ingred = Ingredients.objects.filter(dish__name=name)
        serializer = IngredientsSerializer(ingred, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryView(APIView):
    def get(self, request, id=None, format=None):
        id = id
        if id is not None:
            cat = Category.objects.get(pk=id)
            serializer = CategorySerializer(cat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            cat = Category.objects.all()
            serializer = CategorySerializer(cat, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemView(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = ItemSerializer

class IngredientView(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer




    
