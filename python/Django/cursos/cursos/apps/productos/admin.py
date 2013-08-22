from django.contrib import admin
from cursos.apps.productos.models import Categoria,Producto

admin.site.register(Categoria)
admin.site.register(Producto)