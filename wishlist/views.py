from django.shortcuts import render


def view_wishlist(request):
    """A view to return to wishlist content page"""

    return render(request, 'wishlist/wishlist.html')
