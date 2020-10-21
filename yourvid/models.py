from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField

from yourvid.helpers import generate_random_string, video_upload_path, random_video_id, thumbnail_upload_path

LANGUAGE_CHOICES = (
    ('DE', 'Deutsch'),
    ('EN', 'English'),
    ('FR', 'French'),
    ('RU', 'Russian'),
)

ACCESS_CHOICES = (
    ('PUBLIC', 'Public'),
    ('NOTLISTED', 'Not Listed'),
    ('PRIVATE', 'Private'),
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=['name'])

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(default=0)


class Video(models.Model):
    video_id = models.CharField(max_length=14, default=random_video_id, unique=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to=video_upload_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_path)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.CharField(max_length=255, choices=ACCESS_CHOICES)

    # create format to show in the video_id and title
    def __str__(self):
        return f"{self.video_id}-{self.title}"

    def rating(self):
        """
        (int) Returns the sum of all voted scores on this Video.
        """
        ratings = self.ratings.all()
        score = 0
        for rating in ratings:
            score += rating.score
        return score


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.user.username} commented on {self.video.title}"
