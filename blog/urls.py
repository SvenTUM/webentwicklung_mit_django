from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:post_id>/', views.detail_view, name="detail"),
    path('videos/', views.videos_view, name="videos"),
]
