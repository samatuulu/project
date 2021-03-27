from django.urls import path, include
from rest_framework import routers

from users.views import registration_view, LoginView

router = routers.DefaultRouter()

app_name = "users"

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', registration_view, name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
