from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required , redirect
from django.views.decorators.csrf import csrf_protect
from .forms import PostForm, CommentForm
from django.contrib import messages



def index(request):
    post = Post.objects.all().order_by("-created")

    context = {
        "posts": post,
    }

    return render(request, "grampost/home.html", context)

@login_required
@csrf_protect
def add_post(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                image = form.cleaned_data["image"],
                image_name = form.cleaned_data["image_name"],
                image_caption = form.cleaned_data["image_caption"],
                author = request.user
            )

            post.save()
            print(post)

            post_name = form.cleaned_data.get("image_name")
            messages.success(request, f'Post created {post_name} !')
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "grampost/new_post.html", {"form": form})







