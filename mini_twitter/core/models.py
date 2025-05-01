from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    conteudo = models.TextField(max_length=280, default='Texto padrão')
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'
