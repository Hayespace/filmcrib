# videos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('featured/', views.featured_videos, name='featured_videos'),
]
