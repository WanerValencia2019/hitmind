from django.contrib import admin
from apps.blog.models import Articulo,Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Articulo)

