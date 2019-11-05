from django.contrib import admin
from .models import Estabelecimento, Categoria, Produto, Dono_estabelecimento

admin.site.register(Categoria)
admin.site.register(Estabelecimento)
admin.site.register(Produto)
admin.site.register(Dono_estabelecimento)