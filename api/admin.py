from django.contrib import admin
from .models import Category, Dishes, Ingredients


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ['cat', 'name', 'desc', 'created_by']


@admin.register(Ingredients)
class IngedientsAdmin(admin.ModelAdmin):
    list_display = ['dish', 'rules']