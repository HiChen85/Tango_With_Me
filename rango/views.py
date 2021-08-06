import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from rango.models import WebSiteCategory, Page, Video
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import time
import re
# Create your views here.
from tango_with_me import settings


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

@login_required
def profile(request):
    # if request.method == 'POST':

    return render(request, "rango/user-profile.html")


@login_required
def add_video(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        video = Video()
        iframe_url = request.POST.get('iframe_url')
        title = request.POST.get('video_title')
        video.user = user
        video.iframe_url = iframe_url
        video.title = title
        video.save()
        return redirect(reverse('rango:videos'))
    return render(request, 'rango/index.html')

@login_required
def videos(request):
    pattern = r'src=.+"\s[titlescrolling]'
    context = {}
    user = User.objects.get(username=request.user.username)
    videos = Video.objects.filter(user=user)
    video_url_list = []
    for v in videos:
        substr = re.search(pattern, v.iframe_url)
        url = substr.group().split(' ')[0].split('"')[1]
        print(url)
        video_url_list.append((v.title, url))

    context['video_urls'] = video_url_list
    return render(request, 'rango/videos.html', context=context)


def about(request):
    return render(request, 'rango/about.html')

@login_required
def like_up(request):
    context_dict = {}
    if request.method == 'POST':
        mod = request.POST.get('mod')
        if mod == 'WebSiteCategory':
            name = request.POST.get('name').strip()
            print('yes')
            obj = WebSiteCategory.objects.get(name=name)
            obj.likes += 1
            obj.save()
            current_likes = WebSiteCategory.objects.get(name=name).likes
            context_dict = {'likes': current_likes}
            print(context_dict)
        if mod == 'Page':
            title = request.POST.get('title').strip()
            print('no')
            obj = Page.objects.get(title=title)
            obj.likes += 1
            obj.save()
            current_likes = Page.objects.get(title=title).likes
            context_dict = {'likes': current_likes}
            print(context_dict)
    return JsonResponse(context_dict)

def add_view(request):
    context_dict = {}
    if request.method == 'POST':
        mod = request.POST.get('mod')
        if mod == 'WebSiteCategory':
            name = request.POST.get('name').strip()
            print('YES')
            obj = WebSiteCategory.objects.get(name=name)
            obj.views += 1
            obj.save()
            current_views = WebSiteCategory.objects.get(name=name).views
            context_dict = {'views': current_views}
            print(context_dict)
        if mod == 'Page':
            title = request.POST.get('title').strip()
            print('no')
            obj = Page.objects.get(title=title)
            obj.views += 1
            obj.save()
            current_views = Page.objects.get(title=title).views
            context_dict = {'views': current_views}
            print(context_dict)
        return JsonResponse(context_dict)

@csrf_exempt
def upload_img(request):
    image = request.FILES.get('file')
    path_image = settings.STATIC_DIR +  "/image_user/"
    image_name1 = str(int(round(time.time()*1000)))
    image_path = path_image+image_name1+'.jpg'
    print(image_path)
    if not os.path.exists(image_path):
        print(123)
        with open(image_path, 'wb') as f:
            f.write(image.read())
            f.close()
    else:
        return HttpResponse("false")
    return HttpResponse(image_path)