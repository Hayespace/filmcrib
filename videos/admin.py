# videos/admin.py
from django.contrib import admin
from .models import Video, Genre

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_genres', 'rating', 'release_date', 'country', 'director', 'producer', 'featured')
    list_filter = ('genres', 'release_date', 'country', 'featured')
    search_fields = ('name', 'description', 'director', 'producer', 'cast', 'awards')
    filter_horizontal = ('genres',)  # Use filter_horizontal for many-to-many fields

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = 'Genres'

admin.site.register(Video, VideoAdmin)
admin.site.register(Genre)
