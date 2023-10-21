from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import ArticleModelForm

from .models import Article

# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    context_object_name = 'form'

    def form_valid(self, form: BaseModelForm):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
    context_object_name = 'artic'

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)
