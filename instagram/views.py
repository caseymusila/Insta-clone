from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import PostForm, CommentForm



def index(request):
    post = Post.objects.all().order_by("-created")

    context = {
        "posts": post,
    }

    return render(request, "grampost/home.html", context)







