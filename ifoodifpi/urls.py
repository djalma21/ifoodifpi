"""ifoodifpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.viewsets import ListaProdutosViewSet, CategoriaViewSet, ListaEstabelecimentoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ListaProdutosViewSet, base_name='api_produtos')
router.register(r'categoria', CategoriaViewSet, base_name='api_categoria')
router.register(r'estabelecimentos', ListaEstabelecimentoViewSet, base_name='api_estabelecimento')
router.register(r'User', UserViewSet, base_name='api_user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('core.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
