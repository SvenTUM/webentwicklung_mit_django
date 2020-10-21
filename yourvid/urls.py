from django.urls import path

from . import views

app_name = 'yourvid'
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<str:video_id>/', views.detail_view, name="detail"),
    path('comment/add/<str:video_id>/', views.comment_add, name="add-comment"),
]
