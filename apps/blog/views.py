from django.db.models import Q
from django.http import request, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.urls import reverse
from  django.views.generic import CreateView,ListView
from apps.blog.models import Articulo,Categoria
from apps.blog import forms
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.forms import ModelForm

# Create your views here.



class Articulos(CreateView):
    model=Articulo
    template_name ='principal/crear.html'
    form_class = forms.ArticuloForm
    success_url = '../'

class CrearArticulo(ListView):
    model = Articulo
    template_name ='principal/index.html'


#Con esta vemos los articulos el nombre esta malo
def crearArticulo(request):
	queryset=request.GET.get('search')
	object_list=Articulo.objects.all().order_by('fecha').reverse()
	paginator=Paginator(object_list,5)
	try:
		pagina=int(request.GET.get("page",'1'))
	except ValueError:pagina=1
	try:
		object_list=paginator.page(pagina)
	except (InvalidPage,EmptyPage):
		object_list=paginator.page(paginator.num_pages)
	

	if queryset:
		object_list=Articulo.objects.filter(Q(titulo__icontains=queryset) | Q(autor__icontains=queryset))
			
	return render(request,'principal/index.html',{'object_list':object_list})




def verARTICULO(request,pk):
	identrada=Articulo.objects.get(pk=int(pk)) #le estoy pasando como articulo el id de entrada pra poder usarlo en el template
	return  render_to_response("principal/verArticulo.html",dict(articulo=identrada,usuario=request.user))


class Tecnología(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="tecnologia"))
		context_object_name='tecnologia'
		template_name="categorias/tecnologia.html"
class Deportes(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="deportes"))
		context_object_name='deportes'
		template_name="categorias/deportes.html"
class Religion(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="religion"))
		context_object_name='religion'
		template_name="categorias/religion.html"

class Ciencia(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="ciencia"))
		context_object_name='ciencia'
		template_name="categorias/ciencia.html"
class Programacion(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="programacion"))
		context_object_name='programacion'
		template_name="categorias/programacion.html"
class ActualidadMundial(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="actualidad mundial"))
		context_object_name='ActualidadMundial'
		template_name="categorias/ActualidadMundial.html"
class Politica(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="politica"))
		context_object_name='politica'
		template_name="categorias/politica.html"

class Musica(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="musica"))
		context_object_name='musica'
		template_name="categorias/musica.html"
class Choco(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="choco-colombia"))
		context_object_name='choco'
		template_name="categorias/choco.html"
class Entretenimiento(ListView):
		paginate_by = 4
		model=Articulo
		queryset=Articulo.objects.filter(Q(categorias__categoria="entretenimiento"))
		context_object_name='entretenimiento'
		template_name="categorias/entretenimiento.html"











