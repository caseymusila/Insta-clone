from django.shortcuts import render
from .models import Post, Comment

def index(request):
    post = Post.objects.all().order_by("-created")

    context = {
        "posts": post,
    }

    return render(request, "grampost/home.html", context)



# Create your views here.
