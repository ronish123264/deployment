from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')

        Post.objects.create(title=title, content=content, author=author)
        return redirect('posts:post_list')
    return render(request, 'posts/post_create.html')

def post_update(request, id):
    post= Post.objects.get(id=id)
    if request.method == 'POST':
        post.title =request.POST.get('title')
        post.content =request.POST.get('content')
        post.author =request.POST.get('author')
        post.save()
        return redirect('posts:post_list')
    return render(request, 'posts/post_update.html', {'post':post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:post_list')
    
    return render(request, 'posts/post_delete.html', {'post':post})
    