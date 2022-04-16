from django.shortcuts import render


def index(request):
    """A view to return to index page"""
    return render(request, 'home/index.html')
