

# Create your views here.

from django.shortcuts import render
from .models import Laptop

def laptop_home(request):
    laptops = Laptop.objects.all()

    return render(request, 'laptops.html', {
        'laptops': laptops
    })
