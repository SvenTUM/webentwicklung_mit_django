from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def index(request):
    first_post = BlogPost.objects.first()
    context = {
        'blogpost': first_post,
    }
    return render(request, 'blog/index.html', context=context)
