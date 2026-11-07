from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.title}'

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.TextField()
    Film = models.OneToOneField(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Film.title}'

class Director(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    Film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Film.title}'

class Actors(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    Film = models.ManyToManyField(Film)

    def __str__(self):
        return f'{self.Film}'