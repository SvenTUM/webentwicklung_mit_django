from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('post/create/', views.CreatePost.as_view(), name="create-post"),
    path('post/retrieve/<int:pk>/', views.RetrievePost.as_view(), name="retrieve-post"),
    path('post/update/<int:pk>/', views.UpdatePost.as_view(
        success_url='/blog/post/retrieve/%(pk)/'), name="update-post"),
    path('post/delete/<int:pk>/', views.DeletePost.as_view(), name="delete-post"),
    path('st/', views.StaticView.as_view(), name="static-template"),
]
