from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        created_at = request.POST.get('created_at')
        contact = Contact(name=name, phone=phone,email=email, message=message, created_at=created_at)
        contact.save()
    return render(request, 'pages/contact.html')

# Create your views here.
