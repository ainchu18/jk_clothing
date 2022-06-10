from django.shortcuts import render
from .models import Contact
from django.contrib import messages


def contactForm(request):

    if request.method == 'POST':
        contact = Contact()
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
