from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(verbose_name='Name of the movie', max_length=50)
    synthesis = models.TextField(verbose_name='Movie Synthesis', max_length=1000)
    director = models.CharField(verbose_name='Directed by', max_length=500)
    protagonist = models.CharField(verbose_name='Protagonists', max_length=500)
    picture = models.ImageField(upload_to='Insert Picture')
    rating = models.CharField(verbose_name='Movie rating', max_length=3)
    duration = models.DecimalField(verbose_name='Movie length', max_digits=6, decimal_places=2)


class Score(models.Model):
    like = models.BooleanField(verbose_name='Do you liked the movie?', default=False)


class Comment(models.Model):
    insert = models.TextField(verbose_name='Add Comment', max_length=1000)
    answer = models.TextField(verbose_name='Add reply to comment', max_length=1000)
    like = models.BooleanField(verbose_name='Do you like the comment?', default=False)
