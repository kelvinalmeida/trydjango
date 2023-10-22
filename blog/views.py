from typing import Any
from django.db import models
from django.urls import reverse
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleModelForm

from .models import Article

from django.views import View

# Create your views here.

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/about.html', {})


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    context_object_name = 'form'

    def form_valid(self, form: BaseModelForm):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()
    context_object_name = 'form'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
    context_object_name = 'artic'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # queryset = Article.objects.all()
    context_object_name = 'object'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
    
    def get_success_url(self) -> str:
        return reverse('article:article-list')
 