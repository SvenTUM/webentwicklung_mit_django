from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from yourvid.models import Category, Video


def index(request):
    all_categories = Category.objects.all()
    latest_videos = Video.objects.order_by('-upload_date')
    context = {
        'categories': all_categories,
        'videos': latest_videos,
    }
    return render(request, 'yourvid/index.html', context=context)


def detail_view(request, video_id):
    return HttpResponse('')
