from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rango.models import Page


def search_do(request):
    search_item = request.GET.get('search')
    pages = Page.objects.filter(title__icontains=search_item)
    context = {}
    context['current_page'] = pages
    context['search_item'] = search_item
    return render(request, "rango/search.html", context=context)

# @csrf_exempt
# def search(request):
#     if request.POST:
#         pages = Page.objects.all()
#         if pages==None:
#             return HttpResponse("null")
#         return HttpResponse(pages)
