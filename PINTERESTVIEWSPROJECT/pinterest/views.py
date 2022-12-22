from django.shortcuts import render
from django.http import HttpResponse
from .models import Pinterest

def home(request):
 searchTerm = request.GET.get('searchPinterest')
 return render(request, 'home.html', 
 {'searchTerm':searchTerm})

def about(request):
 return render(request, 'about.html')

def signup(request):
 email = request.GET.get('email')
 return render(request, 'signup.html', {'email':email})

# Create your views here.
