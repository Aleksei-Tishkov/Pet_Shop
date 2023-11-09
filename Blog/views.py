from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from Blog.models import Post, PostTag
from Blog.forms import AddPostForm
from django.utils import translation


class BlogView(ListView):
    template_name = 'Blog/Blog.html'
    extra_context = {
        'title': 'Pet Blog'
    }
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class TagView(ListView):
    template_name = 'Blog/Tags.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = PostTag.objects.get(tag_slug=self.kwargs['tag_slug'])
        context['title'] = tag.tag_name.title() + ' tag'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True).filter(tags__tag_slug=self.kwargs['tag_slug'])


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