from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article.models import Article, Category


# Create your views here.


class ArticleList(ListView):
    template_name = 'article/article-list.html'
    model = Article
    paginate_by = 1
    context_object_name = 'articles'

    def get_queryset(self):
        query = super().get_queryset()

        category_name = self.kwargs.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ArticleDetail(DetailView):
    template_name = 'article/article-detail.html'
    model = Article
    context_object_name = 'article'


def category_sidebar_component(request):
    categories = Category.objects.filter(published=True).all()
    return render(request, 'article/components/category-component.html', {'categories': categories})
