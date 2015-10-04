from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
        return render_to_response ("bytebloksite/home.html")

def sitedown(request):
        return render_to_response ("bytebloksite/sitedown.html")

def dev(request):
        return render_to_response ("bytebloksite/dev.html")