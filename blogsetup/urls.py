from django import views
from django.contrib import admin
from django.urls import path
from . import views
from .views import RegistroBlog

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca/', views.acerca, name="acerca"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', RegistroBlog.as_view(), name="registro"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('cerrarsesion', views.cerrarsesion, name="cerrarsesion"),
    path('blogpost/<int:contenido_id>/', views.blogpost, name="blogpost"),
    path('crearpost/', views.crearpost, name="crearpost"),
    path('listado/', views.listado, name="listado"),
    path('editarpost/<int:contenido_id>/', views.editar, name="editar"),
    path('eliminar/<int:conteido_id>/', views.eliminar, name="eliminar"), 

]