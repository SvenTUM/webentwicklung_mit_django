from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from yourvid.models import Category, Video, Vote


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

        # Create Votes
        Vote.objects.create(user=u1, video=Video.objects.first(), score=1)
        Vote.objects.create(user=u2, video=Video.objects.first(), score=1)
        Vote.objects.create(user=u3, video=Video.objects.first(), score=5)

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

    def test_video_count(self):
        count = Video.objects.count()
        self.assertEqual(count, 1)

    def test_vote_count(self):
        count = Vote.objects.count()
        self.assertEqual(count, 3)

    def test_vote_links(self):
        obj = Vote.objects.get(pk=1)
        user = User.objects.get(username="Foo")
        video = Video.objects.first()
        self.assertEqual(obj.user, user)
        self.assertEqual(obj.video, video)
        self.assertEqual(obj.score, 1)

    def test_vote_accumulation(self):
        """
        Should have a score of 7 as this is the sum of the scores of all the Votes.
        """
        video = Video.objects.get(pk=1)
        video_ratings = video.ratings.all()
        video_score = 0
        for rating in video_ratings:
            video_score += rating.score
        self.assertEqual(video_score, 7)

    def test_video_count(self):
        count = Video.objects.count()
        self.assertEqual(count, 1)

    def test_video_str(self):
        obj = Video.objects.first()
        self.assertEqual(str(obj), f"{obj.video_id}-{obj.title}")

    def test_video_rating(self):
        obj = Video.objects.first()
        self.assertEqual(obj.rating(), 7)
