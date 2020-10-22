from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from blog.models import BlogPost


class IndexView(ListView):
    model = BlogPost
    paginate_by = 2


class StaticView(TemplateView):
    template_name = "blog/static.html"
    extra_context = {
        'my_var': "Ein anderer String"
    }


class CreatePost(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = (
        'title',
        'text',
        'publish_date',
        'author',
    )
    success_url = reverse_lazy('blog:retrieve-post')


class RetrievePost(DetailView):
    model = BlogPost


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = (
        'title',
        'text',
    )
    success_url = reverse_lazy('blog:index')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:index')

