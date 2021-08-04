from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={}
    return render(request, "rango/index.html", context=context_dict)

def base(request):
    return render(request, "rango/base.html")

def categories(request):
    return render(request, "rango/categories.html")

def profile(request):
    return render(request, "rango/user-profile.html")

def login(request):
    return render(request, "rango/login.html")

def addCategory(request):
    return render(request, "rango/add-category.html")