# views.py
from django.shortcuts import render
from .models import Genre

def home(request):
    genres = Genre.objects.all()
    print(genres)  # Debug line
    return render(request, 'home/index.html', {'genres': genres})
    