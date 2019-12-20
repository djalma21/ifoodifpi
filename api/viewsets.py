from django.contrib.auth.models import User
from django.template.context_processors import request
from rest_framework.viewsets import ModelViewSet
from .serializer import ProdutoSerializer, CategoriaSerializer, EstabelecimentoSerializer, UserSerializer
from core.models import Produto, Categoria, Estabelecimento
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import  get_object_or_404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django_filters import rest_framework as filters


class ListaProdutosViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListaEstabelecimentoViewSet(ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListPordutoEstabelecimento(ModelViewSet):
     queryset = Produto.objects.filter(estabelecimento=1)
     serializer_class = ProdutoSerializer