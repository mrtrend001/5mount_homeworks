from django.db import models


class Director(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=7)
    director = models.TextField(max_length=100)


class Review(models.Model):
    text = models.CharField(max_length=1000)
    movie = models.CharField(max_length=100)



