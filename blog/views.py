from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy, reverse
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


class CreatePost(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = (
        'title',
        'text',
        'publish_date',
        'author',
    )
    permission_required = ('blog.add_blogpost', )

    def get_success_url(self):
        return reverse('blog:retrieve-post', kwargs={'pk': self.object.pk})
        # alternative with args
        # return reverse('blog:retrieve-post', args=[self.object.pk])


class RetrievePost(DetailView):
    model = BlogPost


class UpdatePost(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = (
        'title',
        'text',
    )
    permission_required = ('blog.change_blogpost', )

    def get_success_url(self):
        return reverse('blog:retrieve-post', kwargs={'pk': self.object.pk})


class DeletePost(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:index')
    permission_required = ('blog.delete_blogpost', )
