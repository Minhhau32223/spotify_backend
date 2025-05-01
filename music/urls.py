from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, chat_with_ai

router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', chat_with_ai, name='chat_with_ai'),
]
