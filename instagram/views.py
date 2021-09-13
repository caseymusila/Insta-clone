from django.shortcuts import render , redirect
from .models import Post , Comment
from django.contrib.auth.decorators import login_required 
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


@login_required
@csrf_protect
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author = user, body = form.cleaned_data["body"], post = post)

            comment.save()

    comments = Comment.objects.filter(post = post).order_by("-created")
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "grampost/post_details.html", context)

@login_required
def like(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()

    return redirect("home")




@login_required
def delete_post(request, id):
    obj = get_object_or_404(Post, id = id)
    if request.method == "POST" and request.user.is_authenticated and request.user.username == User:
        obj.delete()

        messages.success(request, f'Post deleted successfully.')
        return redirect("home")

    context = {}


    return render(request, "grampost/delete_post.html", context)
