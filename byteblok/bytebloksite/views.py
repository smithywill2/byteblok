from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sitedown(request):
        return render_to_response ("bytebloksite/sitedown.html")