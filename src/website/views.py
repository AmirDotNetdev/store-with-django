from django.shortcuts import render
from django.contrib.auth import logout
from .models import *
def home(request):
    return render(request,'home/home.html',)

def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request,'products/products.html',context)

def logout(request):
    logout(request)
    return render(request,'home/home.html')
