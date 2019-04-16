from django.shortcuts import render, redirect, reverse, get_object_or_404
from .utils import imdb_scrapper, get_yt_info
from .utils2 import stars_update, director_update
from .models import Movies, Genre, Star, Director
from django.core.paginator import Paginator


def cat(request):
    genres = Genre.objects.all()
    return render(request, 'navbar.html', {'genres': genres})


def home(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request, 'movies\home.html', {'movies': movies})


def details(request, id):
    detail = get_object_or_404(Movies, pk=id)
    yt_tr = detail.yt_trailer_url
    yt_tr = yt_tr.replace("watch?v=", "embed/")

    director_w = detail.director.weight
    if director_w < 20:
        d = 0.3
    elif director_w >= 20 and director_w < 40:
        d = 0.5
    elif director_w >= 40 and director_w < 60:
        d = 0.7
    elif director_w > 60:
        d = 1

    yt_view = detail.yt_trailer_views
    if yt_view < 20000000:
        ytv = 0.3
    elif yt_view >= 20000000 and yt_view < 50000000:
        ytv = 0.5
    elif yt_view >= 50000000 and yt_view < 100000000:
        ytv = 0.5
    elif yt_view > 100000000:
        ytv = 1

    ph_c = detail.ph_credit
    if ph_c < 20:
        phc = 0.3
    elif ph_c >= 20 and ph_c < 40:
        phc = 0.5
    elif ph_c >= 40 and ph_c < 60:
        phc = 0.7
    elif ph_c > 60:
        phc = 1

    imdb_meta = detail.imdb_meta
    if imdb_meta < 40:
        imdb = 0.3
    elif imdb_meta >= 40 and imdb_meta < 60:
        imdb = 0.5
    elif imdb_meta >= 60 and imdb_meta < 80:
        imdb = 0.7
    elif imdb_meta > 80:
        imdb = 1

    sum = d + ytv + phc + imdb
    result = float(sum) / 4

    if result < 0.2:
        pr = "Disaster"
    elif result >= 0.2 and result < 0.4:
        pr = "Flop"
    elif result >= 0.4 and result < 0.5:
        pr = "Average"
    elif result >= 0.5 and result < 0.6:
        pr = "Hit"
    elif result >= 0.6 and result < 0.8:
        pr = "Super Hit"
    elif result > 0.8:
        pr = "Blockbuster"

    print(result)
    print(pr)

    genres = Genre.objects.all()
    return render(request, 'Movies/details.html', {'detail': detail, 'genres': genres, 'yt_tr': yt_tr, 'pr': pr,
                                                   'result': result})


def search(request):
    keywords = ''
    movies = Movies.objects.all()
    genres = Genre.objects.all()
    stars = Star.objects.all()
    if 'keywords' in request.POST:
        keywords = request.POST['keywords']
        if keywords:
            movies = movies.filter(name__icontains=keywords)
            genres = genres.filter(g_name__icontains=keywords)
            stars = stars.filter(s_name__icontains=keywords)

    return render(request, 'movies/search.html', {'movies': movies, 'keywords': keywords, 'genres': genres, 'stars': stars})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genre/genres.html', {'genres': genres})


def actors(request):
    actors = Star.objects.all()
    paginator = Paginator(actors, 6)  # Show 6 contacts per page
    page = request.GET.get('page')
    actors = paginator.get_page(page)
    return render(request, 'actors/actors.html', {'actors': actors})


def actor_details(request, id):
    actor = get_object_or_404(Star, pk=id)
    return render(request, 'actors/a_details.html', {'actor': actor})


def directors(request):
    directors = Director.objects.all()
    paginator = Paginator(directors, 6)  # Show 6 contacts per page
    page = request.GET.get('page')
    directors = paginator.get_page(page)
    return render(request, 'director/directors.html', {'directors': directors})


def directors_details(request, id):
    director = get_object_or_404(Director, pk=id)
    return render(request, 'director/d_details.html', {'director': director})


def update(request):
    imdb_scrapper()
    return redirect(reverse('home'))


def yt_update(request):
    get_yt_info()
    return redirect(reverse('home'))


def star_update(request):
    stars_update()
    return redirect(reverse('actors'))


def d_update(request):
    director_update();
    return redirect(reverse('directors'))
