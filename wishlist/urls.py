from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name="view_wishlist"),
    path('add-wishlist/', views.add_wishlist, name="add_wishlist"),
    # path('adjust/<item_id>', views.adjust_bag, name="adjust_bag"),
    # path('remove/<item_id>', views.remove_from_bag, name="remove_from_bag"),
]
