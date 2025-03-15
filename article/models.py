from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from account.models import User
from django.core.validators import FileExtensionValidator, MaxValueValidator



class UpdateCreateMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updeted = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(UpdateCreateMixin):
    title = models.CharField(max_length=300)
    url_title = models.CharField(max_length=50, verbose_name='slug')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['created']


class Article(UpdateCreateMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_article')
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50, blank=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='article')
    video = models.FileField(upload_to='article/video', null=True, blank=True, validators=[
         FileExtensionValidator(allowed_extensions=['mp4'], message='Video format must be mp4.'),
        MaxValueValidator(30 * 1024 * 1024, message='Video size should not exceed 30 megabytes.')
    ])
    body = RichTextField()
    tags = models.ManyToManyField('Tag', related_name='tag_article')
    published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}-{self.author}-{self.category}"

    def get_absolute_url(self):
        return reverse('article:article-detail', args=[self.slug])

    def image_tag(self):
        return format_html('<img src = "{}" width=60% height=40px>'.format(self.image.url))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    url_title = models.CharField(max_length=150)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Comment(UpdateCreateMixin):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()

    def __str__(self):
        return f"{self.article} - {self.user} - {self.body}[:20]"
    
    class Meta:
        verbose_name_plural = 'comments'


    
