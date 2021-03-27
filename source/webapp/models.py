from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    text = models.TextField(max_length=1000, null=False, blank=False)
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Articles'


class ArticleLike(models.Model):
    like_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_like')
    like_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='article_like')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)

    def __str__(self):
        return str(self.like_article)

    class Meta:
        verbose_name_plural = 'Article Likes'
