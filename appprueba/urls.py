
from django.urls import path
from . import views

urlpatterns = [
    #path('proyectos/<int:id>', views.hola),
    #path('proyectos/peronchos', views.peron),
    #path('proyectos/<str:peroncha>', views.parametrico),
    #path('proyectos/<int:patron>', views.listado)
    #path('proyectos/<int:id>', views.conjason)
    #path('proyectos/<int:id>', views.condb)
    #path('proyectos/pagina/', views.formularios4)
    path('', views.Principal,name="Inicio"),
    path('Nosotros/', views.Nosotros,name="Nosotros"),
    path('Cursos/', views.Cursos,name="Cursos"),
    path('Contactos/', views.Contactos,name="Contactos"),
    path('cursos/Informatica/', views.informatica,name="Informatica"),
    path('cursos/Gastronomia/', views.gastronomia,name="Gastronomia"),
    path('cursos/Agropecuarias/', views.Agropecuarias,name="Agropecuarias"),
    path('cursos/Construcciones/', views.Construcciones,name="Construcciones"),
    path('cursos/Idiomas/', views.Idiomas,name="Idiomas"),
    path('cursos/Limpieza/', views.Limpieza,name="Limpieza"),
    path('cursos/mecanica/', views.mecanica,name="mecanica"),
    path('cursos/Textil/', views.Textil,name="Textil"),
    path('cursos/Estetica/', views.Estetica,name="Estetica"),












]