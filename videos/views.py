# videos/views.py
from django.shortcuts import render
from .models import Genre, Video

def home(request):
    genres = Genre.objects.all()
    return render(request, 'home/index.html', {'genres': genres})

def featured_videos(request):
    try:
        featured_genre = Genre.objects.get(name='Featured Videos')
        featured_videos = Video.objects.filter(featured=True, genres=featured_genre)
    except Genre.DoesNotExist:
        featured_videos = []
    return render(request, 'home/index.html', {'featured_videos': featured_videos})
