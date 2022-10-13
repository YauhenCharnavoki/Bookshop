from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length = 50, help_text = "Enter genre's name")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField(null = False)
    date_of_death = models.DateField(null = True, blank = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(help_text = "Enter short book description")
    genre = models.ManyToManyField(Genre, help_text = "Select genres")
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    amount = models.IntegerField(default = 0)
    price = models.FloatField()
    image = models.ImageField(upload_to = "books/%y/%m/%d", blank = True)

    def __str__(self):
        return self.title

    def get_url_book(self):
        return reverse('view', kwargs={'id' : self.id})

    def add_to_cart(self):
        return reverse('add', kwargs={'id' : self.id})

    def get_image_url(self):
        if self.image:
            return self.image.url


