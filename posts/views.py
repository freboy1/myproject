from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreatePost
# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'posts/posts_list.html', context)

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'posts/post_page.html', context)

@login_required(login_url="/users/login/")
def post_new(request):

    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:list')

    form = CreatePost()
    context = {'form': form}
    return render(request, 'posts/post_new.html', context)