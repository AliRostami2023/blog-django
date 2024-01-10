from rest_framework import serializers
from account.models import User
from article.models import Article, Comment


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'full_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password and confirm must match')
        return data
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('password must greater than 8 char or number')
        return value
    

class ArticleListSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tag = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['created', 'updated']


class CommentListSeralizer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    reply = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


