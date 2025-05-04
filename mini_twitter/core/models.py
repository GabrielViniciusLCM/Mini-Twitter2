from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    conteudo = models.TextField(max_length=280, default='Texto padrão')
    imagem = models.ImageField(upload_to='posts/', null=True, blank=True)
    criado_em = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_curtidos', blank=True)

    def __str__(self):
        return f'{self.autor.username}: {self.conteudo[:20]}'

    def total_likes(self):
        return self.likes.count()
