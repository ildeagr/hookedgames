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
    path('eliminarcarrito', views.eliminarcarrito, name='eliminarcarrito'),
    path('perfil', views.perfil, name='perfil'),
    path('mensaje', views.mensaje, name='mensaje'),

    path('loginempleados', views.loginempleados, name='loginempleados'),
    path('menuempleados', views.menuempleados, name='menuempleados'),
    path('volveralmenuempleados', views.volveralmenuempleados, name='volveralmenuempleados'),
    path('gestion', views.gestion, name='gestion'),

    path('buscarstock', views.buscarstock, name='buscarstock'),
    path('modificarstock', views.modificarstock, name='modificarstock'),
    path('verstockcompleto', views.verstockcompleto, name='verstockcompleto'),

    path('alta_empleado', views.alta_empleado, name='alta_empleado'),
    path('baja_empleado', views.baja_empleado, name='baja_empleado'),
    path('modi_empleado', views.modi_empleado, name="modi_empleado"),
    path('ver_empleado', views.ver_empleado, name="ver_empleado"),


    path('cerrarsesion', views.cerrarsesion, name='cerrarsesion'),

    ]