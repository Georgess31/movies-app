from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Video(models.Model):
    MovieID = models.PositiveIntegerField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100)
    Actor2Name = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=100)

    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('SciFi', 'Sci-Fi'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Animation', 'Animation'),
        ('Other', 'Other'),
    ]
    MovieGenre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(datetime.now().year)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
