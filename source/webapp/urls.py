from django.urls import path, include
from rest_framework import routers

from webapp.views import ArticleViewset, LikeViewset, LikeReports

router = routers.DefaultRouter()
router.register(r'create', ArticleViewset, basename='article')
router.register(r'like_dislike', LikeViewset, basename='like')

app_name = "webapp"

urlpatterns = [
    path('', include(router.urls)),
    path('analitics/', LikeReports.as_view(), name='analitics'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
