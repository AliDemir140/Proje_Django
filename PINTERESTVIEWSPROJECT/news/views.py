from django.shortcuts import render
from .models import News


def news(request):
 return render(request, 'news.html')


# Create your views here.
