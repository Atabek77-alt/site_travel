from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import  TemplateView, CreateView
from .forms import *
from ..posts.models import Post,Tag

from .models import Appeal


# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')[:4]
        context['tags'] = Tag.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'
    model = Appeal
    form_class = ContactForm
    success_url = '/'



