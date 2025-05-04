from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('postar/', views.criar_post, name='criar_post'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('deletar/<int:post_id>/', views.deletar_post, name='deletar_post'),
    path('feed/', views.feed, name='feed'),
    path('seguir/<int:user_id>/', views.seguir_usuario, name='seguir_usuario'),
    path('deseguir/<int:user_id>/', views.deseguir_usuario, name='deseguir_usuario'),
    path('usuario/<int:user_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('post/<int:post_id>/curtir/', views.curtir_post, name='curtir_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)