from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Pinterest, Review
from .forms import ReviewForm


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


def createreview(request, pinterest_id):
    pinterest = get_object_or_404(Pinterest, pk=pinterest_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {'form': ReviewForm(), 'pinterest': pinterest})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.pinterest = pinterest
            newReview.save()
            return redirect('detail', newReview.pinterest.id)
        except ValueError:
            return render(request, 'createreview.html', {'form': ReviewForm(), 'error': 'bad data passed in'})
