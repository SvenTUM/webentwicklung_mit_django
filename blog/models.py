from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=100)  # TODO: reference User Class
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    date_publish = models.DateTimeField()

    def __str__(self):
        return f"#{self.id} - {self.title}"

    def word_count(self):
        return len(self.text.split())


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()