from django.shortcuts import render
from django.views.generic import TemplateView

from article.models import Category


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'


def site_header_component(request):
    categories = Category.objects.filter(published=True).all()
    return render(request, 'shared/site-header-component.html', {'categories': categories})


def site_footer_component(request):
    return render(request, 'shared/site-footer-component.html')
