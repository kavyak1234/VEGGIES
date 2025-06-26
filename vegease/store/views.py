from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('q')
    products = product.objects.filter(name__icontains=query)
    return render(request,'search_results.html', { 'products': products,'query' : query})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST('email')
        password = request.POST('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')  # Or render signup page again

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # After successful signup

    # This will handle GET requests and show the signup form
    return render(request, 'store/signup_result.html')

    

def signin(request):
    query = request.GET.get('q')
    return render(request,'signin_results.html', {'query' : query})
