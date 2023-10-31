from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import Post
from Blog.forms import AddPostForm


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    data = {
        #'author': post.author,
        'title': post.title,
        'main_ph': post.main_photo,
        'summary': post.summary,
        'content': post.content,
        #'autor': post.author,
        'time_create': post.time_create,
        'time_updated': post.time_updated
            }
    return render(request, 'Blog/Post.html', data)


def add_post(request):
    if request.method == 'GET':
        return render(request, 'Blog/Add_post.html', {'form': AddPostForm()})
    form = AddPostForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')     # redirection to post editorial
