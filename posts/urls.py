from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView, CommentDetailView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create', PostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/<slug:slug>', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('comments/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('delete/<int:pk>/<slug:slug>', PostDeleteView.as_view(), name='post-delete'),
]
