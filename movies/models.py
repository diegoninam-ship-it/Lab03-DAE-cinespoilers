from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(default=90)  # IMPORTANTE
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)

    genres = models.ManyToManyField(Genre, related_name='movies')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title