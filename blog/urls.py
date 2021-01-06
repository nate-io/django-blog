from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView
)
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', login_required(PostCreateView.as_view()), name='post-create'),
    path('about/', views.about, name='blog-about')
]