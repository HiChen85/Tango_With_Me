from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name="index"),
    # path('base/', views.base, name="base"),
    path('categories/', views.categories, name="categories"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('add_category/', views.addCategory, name="add_category"),
]