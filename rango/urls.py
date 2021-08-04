from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/', views.categories, name="categories"),
    path('pages/', views.pages, name='pages'),
    path('profile/', views.profile, name="profile"),
    path('add_category/', views.add_category, name="add_category"),
    path('about/', views.about, name='about'),
    path('show_category/<str:category_name>/', views.show_category, name='show_category'),
    path('add_video/', views.add_video, name='add_video'),
    path('videos/', views.videos, name='videos')
]