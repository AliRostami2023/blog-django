from typing import Any

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import Article
from article.models import Category


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['random_post'] = Article.objects.order_by('?')[:1]
        context['most_views'] = Article.objects.all().order_by('-views')[:3]
        context['articles'] = Article.objects.all().order_by('-created')[:7]
        return context


def search(request: HttpRequest):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 12)
    object_list = paginator.get_page(page_number)
    return render(request, 'home/search.html', {'articles': object_list})


def site_header_component(request):
    categories = Category.objects.filter(published=True).all()
    return render(request, 'shared/site-header-component.html', {'categories': categories})


def site_footer_component(request):
    return render(request, 'shared/site-footer-component.html')
