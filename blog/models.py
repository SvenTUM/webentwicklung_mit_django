from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()

    def __str__(self):
        return f"#{self.id} - {self.title}"

    def word_count(self):
        return len(self.text.split())

    class Meta:
        permissions: [
            ('publish_blogpost', 'Publish Blogposts.'),
        ]
