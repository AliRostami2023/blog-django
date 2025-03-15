from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import Article
from article.models import Category
from site_setting.models import Setting, Adver



class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_post'] = Article.objects.order_by('?')[:1]
        context['most_views'] = Article.objects.all().order_by('-views')[:3]
        context['articles'] = Article.objects.all().order_by('-created')[:7]
        context['adver'] = Adver.objects.filter(active=True).first()
        return context


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 12)
    object_list = paginator.get_page(page_number)
    return render(request, 'home/search.html', {'articles': object_list})


def site_header_component(request):
    setting = Setting.objects.filter(active=True).first()
    categories = Category.objects.filter(published=True).all()
    return render(request, 'shared/site-header-component.html', {'categories': categories, 'setting': setting})


def site_footer_component(request):
    setting = Setting.objects.filter(active=True).first()
    return render(request, 'shared/site-footer-component.html', {'setting': setting})

