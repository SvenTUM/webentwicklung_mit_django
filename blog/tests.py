from django.test import TestCase
from django.utils import timezone

from .models import BlogPost


# Create your tests here.
class ModelsTestCase(TestCase):

    def setUp(self):
        target_date = timezone.now() + timezone.timedelta(days=1)
        # Create 2 Posts
        b1 = BlogPost.objects.create(title="First Post", text="Lorem", author="Foo",
                                     date_created=timezone.now(), date_publish=target_date)
        b2 = BlogPost.objects.create(title="Second Post", text="Ipsum", author="Foo",
                                     date_created=timezone.now(), date_publish=target_date)

    def test_object_count(self):
        count = BlogPost.objects.count()
        self.assertEqual(count, 2)
