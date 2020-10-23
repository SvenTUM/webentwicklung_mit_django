from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import BlogPostSerializer
from ..models import BlogPost


class BlogPostViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
