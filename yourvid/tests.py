from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from yourvid.models import Category, Video


class YourvidTestCase(TestCase):

    # Load Video as Fixture
    fixtures = ['sample2.json']
    # +1 User
    # +1 Video
    # +1 Category

    def setUp(self):
        # Create Users
        u1 = User.objects.create(username="Foo")
        u2 = User.objects.create(username="Bar")
        u3 = User.objects.create(username="Baz")

        # Create Categories
        cat1 = Category.objects.create(name="Wirtschaft")
        cat2 = Category.objects.create(name="Politik")
        cat3 = Category.objects.create(name="Sport")
        cat4 = Category.objects.create(name="Übrige Kategorien")

    def test_user_count(self):
        count = User.objects.count()
        self.assertEqual(count, 4)

    def test_category_count(self):
        count = Category.objects.count()
        self.assertEqual(count, 5)

    def test_category_values(self):
        obj = Category.objects.get(pk=5)
        # Key +1 because of fictures
        self.assertEqual(obj.name, "Übrige Kategorien")
        self.assertEqual(obj.slug, "ubrige-kategorien")
