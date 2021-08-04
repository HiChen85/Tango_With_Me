from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from rango.models import WebSiteCategory, Page

# Create your views here.
def index(request):
    web_site_categories = WebSiteCategory.objects.order_by('-views')[:5]
    pages = Page.objects.order_by('-likes')[:5]

    context = {}
    context['web_site_categories'] = web_site_categories
    context['pages'] = pages
    return render(request, "rango/index.html", context=context)

def show_category(request, category_name):
    context = {}
    try:
        web_site_category = WebSiteCategory.objects.get(name=category_name)
        pages = Page.objects.filter(web_site_category=web_site_category)
        context['web_site_category'] = web_site_category
        context['pages'] = pages
    except WebSiteCategory.DoesNotExist:
        context['web_site_category'] = None
        context['pages'] = None
    
    return render(request, 'rango/show_category.html', context=context)


def categories(request):
    context = {}
    all_categories = WebSiteCategory.objects.all()
    context['all_categories'] = all_categories
    return render(request, "rango/categories.html", context=context)

def pages(request):
    context = {}
    pages = Page.objects.all()
    
    current_page_num = request.GET.get('current_page', 1)
    paginator = Paginator(pages, 3)
    current_page = paginator.page(int(current_page_num))
    context['current_page'] = current_page
    return render(request, 'rango/pages.html', context=context)

def profile(request):
    return render(request, "rango/user-profile.html")


def add_category(request):
    return render(request, "rango/add-category.html")

def add_video(request):
    if request.method == 'POST':
        iframe_link = request.POST.get('iframe_link')
        print(iframe_link)
        return redirect(reverse('rango:index'))


def videos(request):
    context = {}

    return render(request, 'rango/videos.html', context=context)


def about(request):
    return render(request, 'rango/about.html')