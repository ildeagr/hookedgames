from django.urls import path
from webgame import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('iniciosesion', views.login, name='login'),
    path('registro', views.registro, name='registrarse'),

    path('catalogo', views.catalogo, name='catalogo'),
    path('volvercatalogo', views.volvercatalogo, name='volvercatalogo'),
    path('nuevocliente', views.nuevocliente, name='nuevocliente'),
    path('contacto', views.contacto, name='contacto'),
    path('vercarrito', views.vercarrito, name='vercarrito'),
    path('agregarcarrito', views.agregarcarrito, name='agregarcarrito'),
    path('perfil', views.perfil, name='perfil'),
    path('mensaje', views.mensaje, name='mensaje'),

    path('loginempleados', views.loginempleados, name='loginempleados'),
    path('menuempleados', views.menuempleados, name='menuempleados'),
    path('gestion', views.gestion, name='gestion'),
    path('gestionventas', views.gestionventas, name='gestionventas'),

    path('buscarstock', views.buscarstock, name='buscarstock'),
    path('modificarstock', views.modificarstock, name='modificarstock'),
    path('verstockcompleto', views.verstockcompleto, name='verstockcompleto'),

    path('cerrarsesion', views.cerrarsesion, name='cerrarsesion'),

    ]