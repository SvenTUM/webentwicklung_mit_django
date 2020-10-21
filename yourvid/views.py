from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from yourvid.forms import CommentForm
from yourvid.models import Category, Video, Comment


# Create your views here.


def index(request):
    all_categories = Category.objects.all()
    latest_videos = Video.objects.order_by('-upload_date')[0:20]
    context = {
        'categories': all_categories,
        'videos': latest_videos,
    }
    return render(request, 'yourvid/index.html', context=context)


@login_required
def detail_view(request, video_id):
    video = Video.objects.get(video_id=video_id)
    context = {
        'video': video,
        'form': CommentForm()
    }
    return render(request, 'yourvid/detail.html', context=context)


def comment_add(request, video_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        video = Video.objects.get(video_id=video_id)
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                text=form.cleaned_data["text"],
                video=video,
            )
            return redirect('yourvid:detail', video_id)
    return redirect('yourvid:index')
