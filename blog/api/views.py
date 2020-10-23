from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .serializers import BlogPostSerializer
from ..models import BlogPost


class BlogPostViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                      UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
