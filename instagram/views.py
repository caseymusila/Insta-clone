from django.shortcuts import render , redirect ,get_object_or_404
from .models import Post , Comment , Profile
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_protect
from .forms import PostForm, CommentForm , RegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User



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


@csrf_protect
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            for user in User.objects.all():
                Profile.objects.get_or_create(user = user)

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been Created for {username}! You can now log in.')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form":form})


@login_required
@csrf_protect
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect("profile")

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    user_post = Post.objects.filter(author=request.user).order_by("-created")
    post = Post.objects.filter(author=request.user).order_by("-created")

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "user_post": user_post,
        "posts": post
    }

    return render(request, "registration/profile.html", context)