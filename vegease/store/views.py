from django.shortcuts import render
from .models import Product

def search(request):
    return render(request,'search_results.html')
def home(request):
    products = [
        {
            "name": "Mango Dasheri",
            "weight": "700 Gm",
            "original_price": 70,
            "discounted_price": 48.13,
            "discount": 31,
            "image_url": "/static/images/mango-dasheri.jpg"
        },
        {
            "name": "Plum",
            "weight": "500 Gm",
            "original_price": 100,
            "discounted_price": 75,
            "discount": 25,
            "image_url": "/static/images/plum.jpg"
        },
        # Add more products similarly...
    ]
    return render(request, 'index.html', {'products': products})
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})