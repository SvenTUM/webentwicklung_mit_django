from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def index(request):
    first_post = BlogPost.objects.first()
    response = ""
    response += "<h2>"
    response += first_post.title
    response += "</h2>"
    response += "Created: " + str(first_post.date_publish)
    response += "<hr"
    return HttpResponse(response)
