from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from article.models import Article, Category


# Create your views here.


class ArticleList(ListView):
    template_name = 'article/article-list.html'
    model = Article
    paginate_by = 10
    context_object_name = 'articles'

    def get_queryset(self):
        query = super().get_queryset()

        category_name = self.kwargs.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article/article-detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        session_key = f"viewed_article {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True
        return super(ArticleDetail, self).get_context_data(**kwargs)


def category_sidebar_component(request):
    categories = Category.objects.filter(published=True).all()
    return render(request, 'article/components/category-component.html', {'categories': categories})

