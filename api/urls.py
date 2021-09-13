from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('itemapi', views.ItemView, basename="itemapi")


urlpatterns = [
    path('', include(router.urls)),
    path('catdishapi/', views.CatDishView.as_view()),
    path('catapi/<str:title>', views.RetreiveCatDishView.as_view()),
    path('dishapi/', views.DishView.as_view()),
    path('dishapi/<int:pk>',views.RetreiveDishView.as_view()),
    path('catdishapi/dishapi/ingredient/<str:name>/', views.singleDishView.as_view()),
    path('catapi/', views.CategoryView.as_view()),
    path('catapi/<int:id>', views.CategoryView.as_view()),
    path('ingredientapi/', views.IngredientView.as_view()),
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
