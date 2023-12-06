from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return f'Категория: {self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название тега')

    def __str__(self):
        return f'Тег: {self.title}'

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    @property
    def tag_list(self):
        return [tag.name for tag in self.tags.all()]

    @property
    def category_name(self):
        try:
            return self.category.name
        except:
            return None

    # @property
    # def filtered_reviews(self):
    #     return Review.objects.filter(product_id=self.id)


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=7)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def clean(self):
        if self.director is not None and not Director.objects.filter(pk=self.director_id).exists():
            raise ValidationError({'director': 'Invalid director ID'})


class Review(models.Model):
    text = models.CharField(max_length=1000)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)




