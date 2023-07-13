from django.urls import path

from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, DraftPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', DraftPostListView.as_view(), name='post_draft_list'),
]