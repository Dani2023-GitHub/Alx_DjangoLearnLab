from django.urls import path
from .views import (
    ProfileView, CustomLoginView, CustomLogoutView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, register,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),    
]
