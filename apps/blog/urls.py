from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.blog import views


urlpatterns = [
	path('articulos/categoria/tecnologia',views.Tecnología.as_view(),name="tecnologia"),
    path('articulos/categoria/deportes',views.Deportes.as_view(),name="deportes"),
    path('articulos/categoria/religion',views.Religion.as_view(),name="religion"),
    path('articulos/categoria/ciencia',views.Ciencia.as_view(),name="ciencia"),
    path('articulos/categoria/programacion',views.Programacion.as_view(),name="programacion"),
    path('articulos/categoria/ActualidadMundial',views.ActualidadMundial.as_view(),name="actualidad"),
    path('articulos/categoria/politica',views.Politica.as_view(),name="politica"),
    path('articulos/categoria/ActualidadChocoana',views.Choco.as_view(),name="choco"),
    path('articulos/categoria/Música',views.Musica.as_view(),name="musica"),
    path('articulos/categoria/Entretenimiento',views.Entretenimiento.as_view(),name="entretenimiento"),
    path('crear/',login_required(views.Articulos.as_view()),name="crear"),
    path(r'^articulo/(?P<pk>\d+)/$',views.verARTICULO,name="verARTICULO" ),
    path(r'',views.crearArticulo,name='listar'),
]
