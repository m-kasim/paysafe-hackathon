from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

def index(request):
    # Render
    return render(request, 'index.html')