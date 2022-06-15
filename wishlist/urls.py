from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name="view_wishlist"),
    path('add-wishlist/', views.add_wishlist, name="add_wishlist"),
    path('delete_wishlist/', views.delete_wishlist, name="delete_wishlist"),
]
