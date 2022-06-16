from django.shortcuts import render


def index(request):
    """A view to return to index page"""
    return render(request, 'home/index.html')


def handle_error(request, exception):
    return render(request, 'custom-404-page.html')
