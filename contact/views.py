from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def contact_form(request):
    """A view where users/shoppers can leave a comment or questions"""
    contact = Contact()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject

        contact.save()
        messages.success(request, 'Thanks for contacting us! We will contact you as soon as possible.')
        return render(request, 'home/index.html')
    else:
        return render(request, 'contact/contact.html')
