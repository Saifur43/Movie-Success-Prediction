from django.db import models


class Star(models.Model):
    s_name = models.CharField(max_length=30, blank=True)
    star_link = models.URLField()
    star_img = models.FileField(upload_to='images/', blank=True, null=True)
    insta_followers = models.IntegerField(blank=True, default=0)
    star_insta = models.URLField(blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    about = models.CharField(max_length=450, blank=True)

    def __str__(self):
        return self.s_name


class Genre(models.Model):
    g_name = models.CharField(max_length=30, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.g_name


class Director(models.Model):
    d_name = models.CharField(max_length=30, blank=True)
    director_link = models.URLField()
    d_img = models.FileField(upload_to='images/', blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.d_name


class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    link = models.URLField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
    outline = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    imdb_meta = models.IntegerField(blank=True, default=0)
    genres = models.ManyToManyField(Genre)
    stars = models.ManyToManyField(Star)
    runtime = models.CharField(blank=True, max_length=20)
    yt_trailer_title = models.CharField(max_length=200, blank=True)
    yt_trailer_url = models.URLField(blank=True)
    yt_trailer_views = models.IntegerField()
    yt_trailer_like = models.IntegerField()
    yt_trailer_dislike = models.IntegerField()
    yt_trailer_uploader = models.CharField(max_length=200, blank=True)
    ph_credit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
