from django.shortcuts import render, redirect, get_object_or_404
# from . import forms
from .forms import RegisterForm , PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from blog.forms import RegisterForm

# Create your views here.
def home(request):
    query = request.GET.get('q')
    author = request.GET.get('author')
    posts = Post.objects.filter(is_published = True)
    if query:
        posts = posts.filter(title__icontains = query)
    if author:
        posts = posts.filter(author__username = author)
    posts = posts.order_by('-created_at')
    paginator = Paginator(posts,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{"page_obj":page_obj, "query":query})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully! Please Login')
            return redirect('blog:signup')
        else:
            messages.error(request,'Please correct the errors below')
    else:
        form = RegisterForm()

    return render(request,'registration/signup.html',{"form":form})


@login_required
def profile(request):
    profile = request.user.profile
    posts = Post.objects.filter(author=request.user)
    return render(request,'registration/profile.html',{"profile":profile,"posts":posts})

def post_list(request):
    posts = Post.objects.filter(is_published = True).order_by('-created_at')
    return render(request,'blog/post_list.html',{"posts":posts})

def post_detail(request,slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request,'blog/post_detail.html',{"post":post})


@login_required
def create_post(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('blog:post_detail', slug = post.slug)
    return render(request,'blog/create_post.html',{"form":form})

@login_required
def update_post(request, slug):
    post = get_object_or_404(Post,slug = slug, author = request.user)
    form = PostForm(request.POST or None,request.FILES or None, instance = post)
    if form.is_valid():
        post.save()
        return redirect('blog:post_detail', slug = post.slug)
    return render(request,'blog/update_post.html',{"form":form})

def delete_post(request, slug):
    post = get_object_or_404(Post,slug = slug, author = request.user)
    if request.method == "POST":
        post.delete()
        return redirect('blog:home')
    return render(request,'blog/delete_post.html',{"post":post})

