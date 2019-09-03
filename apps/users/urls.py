from django.urls import path
from django.conf.urls import url
from apps.users import views

urlpatterns = [
    url(r'registrar',views.Registro.as_view(),name='registrar'),
    path('', views.contact, name="contact"),
]