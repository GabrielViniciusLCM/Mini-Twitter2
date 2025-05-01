from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('postar/', views.criar_post, name='criar_post'),
    path('feed/', views.feed, name='feed'),
]