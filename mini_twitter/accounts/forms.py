from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User  # seu modelo customizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # usa o modelo customizado
        fields = ('username', 'email', 'password1', 'password2')
