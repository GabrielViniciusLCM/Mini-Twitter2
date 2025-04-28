from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
