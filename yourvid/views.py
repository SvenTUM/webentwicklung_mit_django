from django.http import HttpResponse
from django.shortcuts import render

from yourvid.models import Category, Video
# Create your views here.


def index(request):
    all_categories = Category.objects.all()
    latest_videos = Video.objects.order_by('-upload_date')[0:20]
    context = {
        'categories': all_categories,
        'videos': latest_videos,
    }
    return render(request, 'yourvid/index.html', context=context)


def detail_view(request, video_id):
    video = Video.objects.get(video_id=video_id)
    context = {
        'video': video,
    }
    return render(request, 'yourvid/detail.html', context=context)
