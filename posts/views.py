from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Status


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'


class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name='draft')
        context['posts_list'] = Post.objects.filter(
            author=self.request.user
        ).filter(
            status=draft_status
        ).order_by('created_on').reverse()
        return context


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ["title", "subtitle", "status", "body"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ["title", "subtitle", "status", "body"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user
