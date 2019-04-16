from django.contrib import admin
from .models import Movies, Star, Director, Genre


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'runtime', 'year', 'link', 'yt_trailer_views', 'imdb_meta')
    list_display_links = ('id', 'name')
    list_filter = ('stars', 'director', 'genres')
    search_fields = ('id', 'name', 'director', 'runtime', 'year', 'stars')
    list_per_page = 10
    ordering = ('id',)


class StarAdmin(admin.ModelAdmin):
    list_display = ('id', 's_name', 'star_link', 'weight', 'insta_followers')
    list_display_links = ('id', 's_name', 'star_link')
    search_fields = ('id', 's_name', 'star_link', 'weight', 'insta_followers')
    list_per_page = 10
    ordering = ('id',)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_name', 'director_link', 'weight')
    list_display_links = ('id', 'd_name', 'director_link')
    search_fields = ('id', 'd_name', 'director_link', 'weight')
    list_per_page = 10
    ordering = ('id',)


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre)
