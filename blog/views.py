from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import ContactForm
from .models import BlogPost, Contact

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


def contact(request):
    if request.method == "GET":
        form = ContactForm()
        context = {'form': form}
        return render(request, 'blog/contact.html', context)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            c = Contact()
            c.first_name = form.cleaned_data["first_name"]
            c.last_name = form.cleaned_data["last_name"]
            c.email = form.cleaned_data["email"]
            c.save()
            messages.success(request, "Contact creation successful.")
            return redirect("blog:index")
        else:
            context = {
                'form': form,
            }
            messages.error(request, "Contact creation failed.")
            return render(request, 'blog/contact.html', context)
