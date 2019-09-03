from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.
class Categoria (models.Model):
    categoria=models.CharField(max_length=20);
    def __str__(self):
        return self.categoria

class Articulo(models.Model):
    titulo=models.CharField(verbose_name="Título",max_length=100);
    autor=models.CharField(verbose_name="Autor",max_length=50);
    fecha=models.DateTimeField(auto_now_add=True,verbose_name="Fecha");
    descripcion=models.TextField(max_length=700,blank=False)
    contenido=models.TextField(verbose_name="Contenido");
    estado=models.BooleanField()
    categorias=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

   
        

