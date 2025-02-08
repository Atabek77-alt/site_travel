from re import search

from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import  ListView, DetailView

from .forms import SearchForm
from .models import Tag
from .models import Post
from django.db.models import Q
# Create your views here.

class PostBlogView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['search_form'] = SearchForm(self.request.GET)
        return context


    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if   search_text  is None:
            return  Post.objects.all()
        q = Post.objects.filter(Q(title__icontains=  search_text )|Q(text__icontains=  search_text ))
        return q





class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


