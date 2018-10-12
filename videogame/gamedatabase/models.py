from django.db import models


class Game(models.Model):

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    review = models.TextField()
