from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article.models import Article


# Create your views here.


class ArticleList(ListView):
    template_name = 'article/article-list.html'
    model = Article
    paginate_by = 1
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    template_name = 'article/article-detail.html'
    model = Article
    context_object_name = 'article'
