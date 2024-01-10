from django.urls import path
from . import views
from rest_framework.authtoken import views as auth


app_name = 'api'
urlpatterns = [
    path('', views.UserListApiView.as_view()),
    path('token/', auth.obtain_auth_token),
    path('create/', views.CreateUserApiView.as_view()),
    path('update/<int:pk>/', views.UpdateRetrieveDestroyApiView.as_view()),
    path('article/', views.ArticleListApiView.as_view()),
    path('article/create/', views.ArticleCreateApiView.as_view()),
    path('article/update/<int:pk>/', views.UpdateArticleApiView.as_view()),
    path('comment-list/', views.CommentListApiView.as_view()),
    path('comment/create/', views.CommentCreateApiView.as_view()),
    path('comment/update/<int:pk>/', views.UpdateCommentApiView.as_view()),
]

