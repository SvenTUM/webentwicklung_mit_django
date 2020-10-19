from django.test import TestCase, Client
from django.utils import timezone

from .models import BlogPost


# Create your tests here.
class BlogPostTestCase(TestCase):

    def setUp(self):
        target_date = timezone.now() + timezone.timedelta(days=1)
        # Create 2 Posts
        b1 = BlogPost.objects.create(title="First Post", text="Lorem", author="Foo",
                                     date_created=timezone.now(), date_publish=target_date)
        b2 = BlogPost.objects.create(title="Second Post", text="Ipsum", author="Foo",
                                     date_created=timezone.now(), date_publish=target_date)
        b3 = BlogPost.objects.create(title="Third Post", text="Already published Post.", author="Foo",
                                     date_created=timezone.now(), date_publish=timezone.now() + timezone.timedelta(days=-1))
        b4 = BlogPost.objects.create(title="Forth Post", text="Already published Post.", author="Foo",
                                     date_created=timezone.now() - timezone.timedelta(days=-1), date_publish=timezone.now() + timezone.timedelta(days=-1))
        b5 = BlogPost.objects.create(title="Fifth Post", text="Already published Post.", author="Foo",
                                     date_created=timezone.now() - timezone.timedelta(days=-2), date_publish=timezone.now() + timezone.timedelta(days=-1))
        c = Client()

    def test_object_count(self):
        count = BlogPost.objects.count()
        self.assertEqual(count, 5)

    def test_index(self):
        """
        Page should be available to anybody.
        """
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_has_post(self):
        """
        Should render posts, who have a publish date in the past.
        """
        c = Client()
        response = c.get('/')
        filtered_post = BlogPost.objects.get(pk=4)
        self.assertEqual(response.context["blogposts"][1], filtered_post)

    def test_first_post_is_newsest(self):
        """
        Should render posts, who have a publish date in the past.
        """
        c = Client()
        response = c.get('/')
        first_listed_post = BlogPost.objects.get(pk=5)
        self.assertEqual(response.context["blogposts"][0], first_listed_post)
