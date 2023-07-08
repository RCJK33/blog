from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    
class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post