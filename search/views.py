from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rango.models import Page


@csrf_exempt
def search(request):
    if request.POST:
        pages = Page.objects.all()
        if pages==None:
            return HttpResponse("null")
        return HttpResponse(pages)