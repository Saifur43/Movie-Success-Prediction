from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>/', views.details, name='details'),
    path('update/', views.update, name='update'),
    path('yt_update/', views.yt_update, name='yt_update'),
    path('d_update/', views.d_update, name='d_update'),
    path('star_update/', views.star_update, name='star_update'),
    path('search/', views.search, name='search'),
    path('genres/', views.genres, name='genres'),
    path('actors/', views.actors, name='actors'),
    path('actors/<int:id>/', views.actor_details, name='actors_details'),
    path('directors/', views.directors, name='directors'),
    path('directors/<int:id>/', views.directors_details, name='directors_details'),
]