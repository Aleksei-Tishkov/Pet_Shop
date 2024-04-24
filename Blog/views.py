from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions, pagination

from Blog.models import Post, PostTag
from Blog.forms import AddPostForm, EditPostForm
from django.utils import translation

from Blog.serializers import PostSerializer
from Blog.services import get_published_posts, get_posts_by_tag, get_tag, get_author, get_posts_by_author, get_all_posts
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
        context['title'] = 'Posts by tag: ' + tag.tag_name.title()
        return context

    def get_queryset(self):
        return get_posts_by_tag(get_published_posts(), self.kwargs['tag_slug'])


class AuthorView(ListView):
    template_name = 'Blog/Tags.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_author(User, self)
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


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'Blog/Add_post.html'
    extra_context = {'title': 'Compose a new post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(self.request.POST['title'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('edit_post', args=(self.object.slug,))


class AddTag(CreateView):
    model = PostTag
    fields = '__all__'
    template_name = 'Blog/Add_tag.html'
    success_url = reverse_lazy('blog_main')
    extra_context = {'title': 'Tag addition form'}


class EditPost(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'Blog/Add_post.html'
    success_url = reverse_lazy('blog_main')
    extra_context = {
        'title': 'Edit your post',
    }

    def get(self, request, *args, **kwargs):
        __object = self.get_object()
        if __object.author != request.user:
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)


class AuthorPage(LoginRequiredMixin, ListView):
    template_name = 'Blog/AuthorPage.html'
    extra_context = {
        'title': f"Editorial"
    }
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return get_posts_by_author(get_all_posts(), self.request.user.user_slug)


class AuthorPostView(PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'Blog/Post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    permission_required = 'post.edit_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagz'] = [t for t in context['post'].tags.all()]
        context['title'] = context['post'].title
        return context

    def get_object(self, queryset=None):
        __object = get_object_or_404(get_all_posts(), slug=self.kwargs[self.slug_url_kwarg])
        if __object and __object.author != self.request.user:
            raise PermissionDenied()
        return __object


class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blog/DeletePost.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog_main')

    def get_object(self, queryset=None):
        __object = get_object_or_404(get_all_posts(), slug=self.kwargs[self.slug_url_kwarg])
        if __object and __object.author != self.request.user:
            raise PermissionDenied()
        return __object


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    ordering = '-time_create'


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = get_published_posts()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination

