from builtins import id

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

def product(request, id):
    

    product = Product.objects.get(id=id)
    context = {'product':product}

    return render(request, 'products/product.html',context)
