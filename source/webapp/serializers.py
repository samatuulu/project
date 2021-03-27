from rest_framework import serializers

from webapp.models import Article, ArticleLike


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'author', )

    def save(self, **kwargs):
        kwargs["author"] = self.fields["author"].get_default()
        return super().save(**kwargs)


class ArticleLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleLike
        fields = ('id', 'like_article', )


class LikeTimePeriod(serializers.ModelSerializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()

    class Meta:
        model = ArticleLike
        fields = ('id', 'like_by', 'like_article', 'date_from', 'date_to', )


class ResponseLikePeriod(serializers.ModelSerializer):

    class Meta:
        model = ArticleLike
        fields = ('id', 'like_by', 'like_article', )
