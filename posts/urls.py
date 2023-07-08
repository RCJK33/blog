from django.urls import path

from .views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('detail/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
]