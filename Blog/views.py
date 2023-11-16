from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from Blog.models import Post, PostTag
from Blog.forms import AddPostForm
from django.utils import translation

from Blog.services import get_published_posts, get_posts_by_tag, get_tag, get_author, get_posts_by_author
from User.models import User


class BlogView(ListView):
    template_name = 'Blog/Blog.html'
    extra_context = {
        'title': 'Pet Blog'
    }
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return get_published_posts()


class TagView(ListView):
    template_name = 'Blog/Tags.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_tag(PostTag, self)
        context['title'] = 'Posts about' + tag.tag_name.title()
        return context

    def get_queryset(self):
        return get_posts_by_tag(get_published_posts(), self.kwargs['tag_slug'])


class AuthorView(ListView):
    template_name = 'Blog/Tags.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_author(User, self)
        print(author.username)
        context['title'] = 'Posts by ' + author.username
        return context

    def get_queryset(self):
        return get_posts_by_author(get_published_posts(), self.kwargs['author'])


class PostView(DetailView):
    model = Post
    template_name = 'Blog/Post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagz'] = [t for t in context['post'].tags.all()]
        context['title'] = context['post'].title
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Post.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPost(FormView):
    form_class = AddPostForm
    template_name = 'Blog/Add_post.html'
    success_url = reverse_lazy('blog_main')
    extra_context = {'title': 'Post addition form 1/2'}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)