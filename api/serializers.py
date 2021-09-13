from rest_framework import serializers
from .models import Category, Dishes, Ingredients

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'dish', 'rules']

class DishesSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(many=True)
    class Meta:
        model = Dishes
        fields = ['id', 'cat', 'name', 'foodimg', 'desc','created_by', 'ingredient']

class CategoryDishSerializer(serializers.ModelSerializer):
    mydish = DishesSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'title', 'mydish']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['id', 'cat', 'name', 'foodimg', 'desc','created_by',]


    

