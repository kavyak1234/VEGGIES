from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'shop/search_results.html', {
        'products': products,
        'query': query
    })
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


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created")
        return redirect('signin')
    return render(request, 'shop/signup.html')


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')
    return render(request, 'shop/signin.html')


def signout_view(request):
    logout(request)
    return redirect('signin')

def category_view(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'store/category.html', {
        'products': products,
        'category_name': category_name
    })