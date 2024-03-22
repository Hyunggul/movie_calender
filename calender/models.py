from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=200)
    prod_year = models.IntegerField()
    runtime = models.IntegerField()
    genre = models.CharField(max_length=30)
    nation = models.CharField(max_length=30)
    director_name = models.CharField(max_length=10)
    director_eng_name = models.CharField(max_length=50)
    actor_name = models.CharField(max_length=100)
    actor_eng_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'movies'

class Poster(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    posterUrl = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'posters'