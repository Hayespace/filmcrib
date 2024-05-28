# home/views.py
from django.shortcuts import render
from videos.models import Genre, Video

def home(request):
    genres = Genre.objects.all()
    videos = Video.objects.all()
    return render(request, 'home/index.html', {'genres': genres, 'videos': videos})


