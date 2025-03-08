from django.shortcuts import render
from .models import Product

def practice_home(request):
    products = Product.objects.all()  # Fetch all items from the database
    return render(request, 'practice/practice_home.html', {'items': products})