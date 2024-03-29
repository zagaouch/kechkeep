from django.shortcuts import render
from .models import Storage
# Create your views here.

def storages(request):
    return render(request, 'storages/storages.html', {'stor':Storage.objects.all()})

def storage(request):
    return render(request, 'storages/storage.html')