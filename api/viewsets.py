from rest_framework.viewsets import ModelViewSet
from .serializer import ProdutoSerializer, CategoriaSerializer
from core.models import Produto, Categoria

class ListaProdutosViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer