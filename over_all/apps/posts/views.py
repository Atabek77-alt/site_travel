from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import Tag


from .models import Post


# Create your views here.

class PostBlogView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()




class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


