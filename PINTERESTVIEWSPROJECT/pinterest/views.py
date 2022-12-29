from django.shortcuts import render
from django.http import HttpResponse
from .models import Pinterest


def home(request):
 searchTerm = request.GET.get('searchPinterest')
 if searchTerm: pinterests =Pinterest.objects.filter(title__icontains=searchTerm)
 else: pinterests = Pinterest.objects.all()
 return render(request, 'home.html',
 {'searchTerm':searchTerm, 'pinterests': pinterests})

def about(request):
    return render(request, 'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def news(request):
 return render(request, 'news.html')

# Create your views here.
