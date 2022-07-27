from django.shortcuts import render,get_object_or_404, redirect
from .models import Store


# Create your views here.

def index(request):
    return render(request, '.html')

def klodi(request):
    return render(request, 'index.html')