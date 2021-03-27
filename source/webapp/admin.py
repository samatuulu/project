from django.contrib import admin

from webapp.models import Article, ArticleLike

admin.site.register(Article)
admin.site.register(ArticleLike)
