from django.urls import path
from . import views

urlpatterns = [
    path("insta/", views.index, name = "home"),
]