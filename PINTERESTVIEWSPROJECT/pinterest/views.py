from django.shortcuts import render
from django.http import HttpResponse
from .models import Pinterest
from django.shortcuts import get_object_or_404


def home(request):
    searchTerm = request.GET.get('searchPinterest')
    if searchTerm:
        pinterests = Pinterest.objects.filter(title__icontains=searchTerm)
    else:
        pinterests = Pinterest.objects.all()
    return render(request, 'home.html',
                  {'searchTerm': searchTerm, 'pinterests': pinterests})


def about(request):
    return render(request, 'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def news(request):
    return render(request, 'news.html')


def detail(request, pinterest_id):
    pinterest = get_object_or_404(Pinterest, pk=pinterest_id)
    return render(request, 'detail.html', {'pinterest': pinterest})
