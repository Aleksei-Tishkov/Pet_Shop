from django.shortcuts import render, get_object_or_404
from Blog.models import Post


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