from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Importe uma view simples
from django.http import HttpResponse

# Função de view para a página inicial
def home(request):
    return HttpResponse("Bem-vindo ao Mini Twitter!")

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/', include('core.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home),  # Adicionando o path vazio para renderizar a página inicial
]
