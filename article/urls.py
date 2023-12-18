from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('detail/<slug:slug>', views.ArticleDetail.as_view(), name='article-detail'),
]

