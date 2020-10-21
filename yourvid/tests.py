from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from yourvid.forms import CommentForm
from yourvid.helpers import generate_random_string
from yourvid.models import Category, Video, Vote, Comment


class HelpersTestCase(TestCase):
    def test_generate_random_string_length(self):
        self.assertEqual(len(generate_random_string(5)), 5)
        self.assertEqual(len(generate_random_string(8)), 8)
        self.assertEqual(len(generate_random_string(12)), 12)
        self.assertEqual(len(generate_random_string(52)), 52)


class YourvidTestCase(TestCase):
    # Load Video as Fixture
    fixtures = [
        'users.json',
        'videos.json',
    ]

    def setUp(self):
        # The following has already been setup by fixtures:
        # +2 User
        # +3 Video
        # +2 Category
        # +2 Comments
        vid = Video.objects.first()

        # Create Users
        u1 = User.objects.create(username="User1")
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

        # Create Comments
        Comment.objects.create(user=u3, text="Comment 1", video=vid)
        Comment.objects.create(user=u3, text="Comment 2", video=vid)
        Comment.objects.create(user=u3, text="Comment 3", video=vid)
        Comment.objects.create(user=u3, text="Comment 4", video=vid)

    def test_user_count(self):
        count = User.objects.count()
        self.assertEqual(count, 5)

    def test_category_count(self):
        count = Category.objects.count()
        self.assertEqual(count, 6)

    def test_category_str(self):
        obj = Category.objects.get(pk=3)
        self.assertEqual(str(obj), "Wirtschaft")

    def test_category_values(self):
        obj = Category.objects.last()
        # Key +1 because of fixtures
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
        user = User.objects.get(username="User1")
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
        self.assertEqual(count, 3)

    def test_video_str(self):
        obj = Video.objects.first()
        self.assertEqual(str(obj), f"{obj.video_id}-{obj.title}")

    def test_video_rating(self):
        obj = Video.objects.first()
        self.assertEqual(obj.rating(), 7)

    def test_comment_count(self):
        count = Comment.objects.count()
        self.assertEqual(count, 6)

    def test_comment_obj(self):
        obj = Comment.objects.last()
        assert type(obj.user) is User
        assert type(obj.video) is Video
        self.assertEqual(obj.text, "Comment 4")

    def test_comment_str(self):
        obj = Comment.objects.last()
        self.assertEqual(str(obj), f"#{obj.id} - {obj.user.username} commented on {obj.video.title}")

    def test_comment_links(self):
        obj = Comment.objects.last()
        user = User.objects.get(username="Baz")
        video = Video.objects.first()
        self.assertEqual(obj.user, user)
        self.assertEqual(obj.video, video)
        self.assertIn(obj, user.comments.all())
        self.assertIn(obj, video.comments.all())

    #
    # Views
    #

    # Index

    def test_index_response(self):
        """
        Page should be available to anybody.
        """
        c = Client()
        response = c.get('/videos/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Yourvid | Index</title>')

    # Detail

    def test_detail_response(self):
        """
        Page should be available to anybody.
        """
        c = Client()
        video = Video.objects.first()
        response = c.get(f"/videos/detail/{video.video_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Yourvid | Detail</title>')
        self.assertEqual(response.context["video"], video)

    def test_detail_renders_comments(self):
        c = Client()
        video = Video.objects.first()
        comment = video.comments.first()
        response = c.get(f"/videos/detail/{video.video_id}/")
        self.assertContains(response, comment.text)

    # Comment Endpoint

    def test_comment_form_view(self):
        c = Client()
        video = Video.objects.first()
        response = c.get(f"/videos/comment/add/{video.video_id}/")
        self.assertEqual(response.status_code, 302)
