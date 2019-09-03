from django import forms
from apps.blog import models

class ArticuloForm(forms.ModelForm):
    class Meta:
        model=models.Articulo
        fields=[
            'titulo',
            'descripcion',
            'autor',
            'contenido',
            'categorias',
        ]
        labels={  
            'titulo':'Titulo ',
            'descripcion':'Descripción',
            'autor':'Creador',
            'contenido':'Contenido',
        }
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control '}),
            'descripcion':forms.Textarea(attrs={'class':'form-control text-justify'}),
            'autor':forms.TextInput(attrs={'class':'form-control '}),
            'contenido':forms.Textarea(attrs={'class':'form-control text-justify'}),
            'categorias':forms.Select(attrs={'class':'form-select '})
        }

