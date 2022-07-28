from django.shortcuts import render,get_object_or_404, redirect
from .models import Store
from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):

    site = Store.objects.get(pk=2)

    return render(request, 'index.html', {'site': site})



#def generic(request):


    #eturn render(request, 'generic.html')



#def elements(request):


 #   return render(request, 'elements.html')
