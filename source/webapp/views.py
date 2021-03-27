from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Article, ArticleLike
from webapp.serializers import ArticleSerializer, ArticleLikeSerializer, LikeTimePeriod, ResponseLikePeriod


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]


class LikeViewset(viewsets.ModelViewSet):
    queryset = ArticleLike.objects.all()
    serializer_class = ArticleLikeSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(like_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response({'status': 'Like deleted'}, status=status.HTTP_204_NO_CONTENT)


class LikeReports(APIView):
    queryset = ArticleLike.objects.all()
    serializer_class = LikeTimePeriod

    def post(self, request, *args, **kwargs):
        serializer = LikeTimePeriod(data=request.data)
        serializer.is_valid(raise_exception=True)
        date_from = serializer.data['date_from']
        date_to = serializer.data['date_to']
        like_period = ArticleLike.objects.filter(created_at__range=(date_from, date_to))
        serializer = ResponseLikePeriod(like_period, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
