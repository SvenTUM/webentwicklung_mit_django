from rest_framework import serializers

from blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

        extra_kwargs = {
            "url": {"view_name": "api:blogpost-detail", "lookup_field": "title"}
        }
