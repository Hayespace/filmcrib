# home/views.py
from django.shortcuts import render
from videos.models import Genre, Video

def home(request):
    genres = Genre.objects.all()
    featured_videos = Video.objects.filter(featured=True)
    return render(request, 'home/index.html', {'genres': genres, 'featured_videos': featured_videos})
