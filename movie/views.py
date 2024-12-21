from django.shortcuts import render,redirect
from .models import *



def movielist(request):
    movies = Movie.objects.all()
    

    context = {
        'movies' : movies,
    }
    return render(request, 'movie/movielist.html',context)



def moviedetail(request, film_id):
    movie = Movie.objects.get(id=film_id)
    

    context = {
        'movie' : movie,
    }
    return render(request, 'movie/movie_detail.html',context)

def add_movie_review(request):
    if not request.user.is_authenticated:
        return
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = request.POST.get('review_text'),
        )
        return redirect ("films", film_id=movie_id)


# Create your views here.


