from django.conf.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name = "home"),
]