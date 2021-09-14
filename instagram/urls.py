from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("new_post/", views.add_post, name = "add_post"),
    path("<int:pk>/", views.post_detail, name = "post_detail"),
    path("<int:pk>", views.like, name = "likes"),
    path("<int:id>/delete", views.delete_post, name = "delete_post"),

]