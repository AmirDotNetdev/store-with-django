from django.shortcuts import render
from django.contrib.auth import logout
from .models import *
def home(request):
    return render(request,'home/home.html',)

def products(request):
    return render(request,'product/product.html')

def logout(request):
    logout(request)
    return render(request,'home/home.html')
