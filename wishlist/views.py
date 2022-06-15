from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import Wishlist
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
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
        messages.error(request, 'Item already in your wishlist')
        data = {
            'bool': False
        }
    else:
        wishlist = Wishlist.objects.create(
            product=product,
            user=request.user
        )
        messages.success(request, 'Item successfully added to your wishlist')
        data = {
            'bool': True    
        }
    return JsonResponse(data)

def delete_wishlist(request):
    if request.method == "POST":
        wl_id = request.POST.get('wl-id')
        Wishlist.objects.filter(pk=wl_id).delete()

        messages.success(request, 'Item successfully deleted from your wishlist')
        return redirect(reverse('view_wishlist'))
