# videos/models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Video(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)  # Reverted back to 'name'
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    director = models.CharField(max_length=254, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=254, null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name 
