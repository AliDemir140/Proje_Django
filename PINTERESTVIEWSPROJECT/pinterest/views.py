from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Pinterest, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    searchTerm = request.GET.get('searchPinterest')
    if searchTerm:
        pinterests = Pinterest.objects.filter(title__icontains=searchTerm)
    else:
        pinterests = Pinterest.objects.all()
        return render(request, 'home.html', {'searchTerm': searchTerm, 'pinterests': pinterests})


def about(request):
    return render(request, 'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def news(request):
    return render(request, 'news.html')


def detail(request, pinterest_id):
    pinterest = get_object_or_404(Pinterest, pk=pinterest_id)
    reviews = Review.objects.filter(pinterest=pinterest)
    return render(request, 'detail.html', {'pinterest': pinterest, 'reviews': reviews}
                  )

@login_required
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

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.pinterest.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.pinterest.id)
