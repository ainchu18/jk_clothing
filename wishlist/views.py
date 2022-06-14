from django.shortcuts import render
from django.http import JsonResponse
from .models import Wishlist
from products.models import Product


def view_wishlist(request):
    """A view to return to wishlist content page"""

    return render(request, 'wishlist/wishlist.html')


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
