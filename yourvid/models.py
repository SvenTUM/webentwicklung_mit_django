from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=['name'])


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(default=0)


class Video(models.Model):
    video_id = models.CharField(max_length=14)
    language = models.CharField(max_length=3)
    title = models.CharField(max_length=255)
    video_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.CharField(max_length=255)

    # create format to show in the video_id and title
    def __str__(self):
        return f"{self.video_id}-{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
