from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from site_setting.models import Adver
from article.models import Article, Category
from django.views import View
from .models import Comment


# Create your views here.


class ArticleList(ListView):
    template_name = 'article/article-list.html'
    model = Article
    paginate_by = 10
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adver'] = Adver.objects.filter(active=True).first()
        context['random_post'] = Article.objects.order_by('?')[:3]
        return context

    def get_queryset(self):
        query = super().get_queryset()

        category_name = self.kwargs.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ArticleDetail(View):
    def get(self, request: HttpRequest, slug):
        article = get_object_or_404(Article, slug=slug)
        session_key = f"viewed_article {article.slug}"
        if not request.session.get(session_key, False):
            article.views += 1
            article.save()
            request.session[session_key] = True

        return render(request, 'article/article-detail.html', {'article': article})

    def post(self, request: HttpRequest, slug):
        article = get_object_or_404(Article, slug=slug)

        reply_id = request.POST.get('reply_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, reply_id=reply_id)
        return render(request, 'article/article-detail.html', {'article': article})


def category_sidebar_component(request):
    categories = Category.objects.filter(published=True).all()
    return render(request, 'article/components/category-component.html', {'categories': categories})
