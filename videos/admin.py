from django.contrib import admin
from .models import Video, Genre

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'rating', 'release_date', 'country', 'director', 'producer')
    search_fields = ('name', 'description', 'director', 'producer', 'cast', 'awards')
    list_filter = ('genre', 'release_date', 'country')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
