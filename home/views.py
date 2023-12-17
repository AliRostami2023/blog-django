from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'


def site_header_component(request):
    return render(request, 'shared/site-header-component.html')


def site_footer_component(request):
    return render(request, 'shared/site-footer-component.html')
