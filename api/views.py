from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CreateUserSerializers, UserListSerializers, ArticleListSerializers, ArticleCreateSerializers, \
    CommentListSeralizer, CommentCreateSerializers
from account.models import User
from article.models import Article, Comment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from django.core.paginator import Paginator


class UserListApiView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        queryset = User.objects.all()
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 1)
        paginator = Paginator(queryset, page_size)
        ser_data = UserListSerializers(instance=paginator.page(page_number), many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class CreateUserApiView(APIView):
    def post(self, request):
        ser_data = CreateUserSerializers(data=request.data)
        if ser_data.is_valid():
            new_user = User()
            new_user.full_name = ser_data.validated_data.get('full_name')
            new_user.email = ser_data.validated_data.get('email')
            new_user.set_password(ser_data.validated_data.get('password'))
            new_user.is_active = True
            new_user.save()

            return Response(ser_data.data, status.HTTP_201_CREATED)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateRetrieveDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserListSerializers


class ArticleListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializers


class ArticleCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializers


class UpdateArticleApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializers


class CommentListApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSeralizer


class CommentCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers


class UpdateCommentApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentListSeralizer
