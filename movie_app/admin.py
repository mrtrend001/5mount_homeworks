from django.contrib import admin
from movie_app.models import Director, Review, Movie, Category, Tag
# Register your models here.

admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)
