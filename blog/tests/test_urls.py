import pytest

from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_index():
    assert reverse("blog:index") == "/blog/"
    assert resolve("/blog/").view_name == "blog:index"


def test_redirect():
    assert reverse("blog:static-template") == "/blog/st/"
    assert resolve("/blog/st/").view_name == "blog:static-template"


# def test_create_post_view():
#     assert reverse('blog:create-post') == '/blog/post/create/'
#     assert resolve('/blog/post/create/') == 'blog:create-post'
#
#
# def test_retrieve_post_view():
#     assert reverse('blog:retrieve-post') == '/blog/post/retrieve/(?P<id>[0-9]+)/'
#     assert resolve('/blog/post/retrieve/') == 'blog:retrieve-post'
#
#
# def test_update_post_view():
#     assert reverse('blog:update-post') == '/blog/post/update/(?P<id>[0-9]+)/'
#     assert resolve('/blog/post/update/') == 'blog:update-post'
#
#
# def test_delete_post_view():
#     assert reverse('blog:delete-post', kwargs={'id': 5}) == '/blog/post/delete/5/'
#     assert resolve('/blog/post/delete/') == 'blog:delete-post'
