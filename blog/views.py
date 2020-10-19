from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import BlogPost


# Create your views here.
def index(request):
    filtered_posts = BlogPost.objects.filter(date_publish__lte=timezone.now()).order_by('-date_created')
    context = {
        'blogposts': filtered_posts,
    }
    return render(request, 'blog/index.html', context=context)

def detail_view(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    context = {
        'blogpost': post,
    }
    return render(request, 'blog/detail.html', context=context)
