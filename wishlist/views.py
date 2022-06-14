from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Wishlist
from products.models import Product
from django.contrib import messages


def view_wishlist(request):
    """A view to return to wishlist content page"""
    wlist = Wishlist.objects.filter(user=request.user).order_by('-id')

    return render(request, 'wishlist/wishlist.html', {'wlist': wlist})


def add_wishlist(request):

    pid = request.GET['product']
    product = Product.objects.get(pk=pid)
    data = {}
    checkw = Wishlist.objects.filter(product=product, user=request.user).count()

    if checkw > 0:
        
        data = {
            'bool': False
        }

    else:
        wishlist = Wishlist.objects.create(
            product=product,
            user=request.user
        )
        data = {
            'bool': True
            
        }
        
    return JsonResponse(data)


