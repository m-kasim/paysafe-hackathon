from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

def detail(request):
    # Render
    return render(request, 'detail.html')