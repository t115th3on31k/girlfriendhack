from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)