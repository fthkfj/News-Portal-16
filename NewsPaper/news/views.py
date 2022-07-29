from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm, Subscribe
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.core.cache import cache
import logging


l1 = logging.getLogger('django')
l2 = logging.getLogger('django.security')
l3 = logging.getLogger('django.request')
l4 = logging.getLogger('django.server')
l5 = logging.getLogger('django.template')
l6 = logging.getLogger('django.db.backends')


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-DateCreation']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'

    def get_object(self, *args, **kwargs):
        l1.error('check1')
        l2.error('check2')
        l3.error('check3')
        l4.error('check4')
        l5.error('check5')
        l6.error('check6')
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['DateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/news/'
    permission_required = ('news.add_post',)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post',)


class Subscribes(PermissionRequiredMixin, CreateView):
    template_name = 'account/email/week_send.html'
    permission_required = ('news.add_post',)
    form_class = Subscribe
    success_url = '/news/'

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial








