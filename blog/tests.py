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
        c = Client()

    def test_object_count(self):
        count = BlogPost.objects.count()
        self.assertEqual(count, 2)

    def test_index(self):
        """
        Page should be available to anybody.
        """
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_has_post(self):
        c = Client()
        response = c.get('/')
        first_obj = BlogPost.objects.first()
        self.assertEqual(response.context["blogpost"], first_obj)
