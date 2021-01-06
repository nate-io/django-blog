from django.shortcuts import render
from django.views.generic import (
  CreateView, 
  DetailView, 
  ListView
)
from .models import Post


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = [ '-date_posted' ]


class PostDetailView(DetailView):
  model = Post


class PostCreateView(CreateView):
  model = Post
  fields = [ 'title', 'content' ]

  # extend form_valid parent method to add auth'd user
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


def about(request):
  context = {
    'title': 'About'
  }
  
  return render(request, 'blog/about.html', context)
