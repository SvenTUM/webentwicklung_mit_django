from django.urls import path

from . import views

app_name = 'yourvid'
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:post_id>/', views.detail_view, name="detail"),
]
