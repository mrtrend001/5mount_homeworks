from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=7)
    director = models.TextField(max_length=100)


class Review(models.Model):
    text = models.CharField(max_length=1000)
    movie = models.CharField(max_length=100)



