from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, User
from .serializers import PostSerializer, UserSerializer
from django.core.paginator import Paginator

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-criado_em')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        return Response({'status': 'post liked'})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.likes.remove(request.user)
        return Response({'status': 'post unliked'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({'status': f'Você está seguindo {user_to_follow.username}'})

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({'status': f'Você deixou de seguir {user_to_unfollow.username}'})

    @action(detail=False, methods=['get'])
    def feed(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
@login_required
def criar_post(request):
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Post.objects.create(autor=request.user, conteudo=conteudo)
            return redirect('feed')
    return render(request, 'posts/criar_post.html')

@login_required
def feed(request):
    posts_list = Post.objects.all().order_by('-criado_em')  # ordena do mais recente ao mais antigo
    paginator = Paginator(posts_list, 5)  # 5 posts por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/feed.html', {'page_obj': page_obj})

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.autor:
        return redirect('feed')

    if request.method == 'POST':
        novo_texto = request.POST.get('conteudo')
        if novo_texto:
            post.conteudo = novo_texto
            post.save()
            return redirect('feed')

    return render(request, 'posts/editar_post.html', {'post': post})

@login_required
def deletar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.autor:
        return redirect('feed')

    if request.method == 'POST':
        post.delete()
        return redirect('feed')

    return render(request, 'posts/confirmar_delete.html', {'post': post})

