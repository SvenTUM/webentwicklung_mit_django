from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:post_id>/', views.detail_view, name="detail"),
    path('contact/', views.contact, name="contact"),
]
