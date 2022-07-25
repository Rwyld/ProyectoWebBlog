from collections import UserList
from enum import auto
from msilib.schema import ListView
from urllib import request
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls import is_valid_path
from .models import *
from .forms import *
from django.views.generic import View, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required




# Create your views here.
def index(request):
    contenidos=reversed(Contenido.objects.all())
    diseñowebs=DiseñoWeb.objects.all()
    categorias=Categoria.objects.all()
    
    mostrar = {"contenidos":contenidos, "diseñowebs":diseñowebs, "categorias":categorias}

    return render(request, "blogsetup/index.html", mostrar)

def acerca(request):
    categorias=Categoria.objects.all()
    return render(request, "blogsetup/acerca.html", {"categorias":categorias})

def blogpost(request, contenido_id):
    contenido=Contenido.objects.get(id=contenido_id)
    categorias=Categoria.objects.all()
    contenidos=reversed(Contenido.objects.all())

    return render(request, "blogsetup/blogposts.html", {"contenido":contenido, "contenidos":contenidos, "categorias":categorias})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    categorias=Categoria.objects.all()
    contenidos=reversed(Contenido.objects.filter(categoria=categoria))

    return render(request, "blogsetup/categoria.html", {"categoria":categoria, "contenidos":contenidos, "categorias":categorias})

def contacto(request):
    categorias=Categoria.objects.all()

    formulario_contacto = ContactoFormulario()

    if request.method=="POST":
        formulario_contacto=ContactoFormulario(data=request.POST)
        if formulario_contacto.is_valid():
            info = formulario_contacto.cleaned_data
            contacto = ContactoFormulario(nombre=info['nombre'],asunto=info['asunto'], email=info['email'], mensaje=info['mensaje'])
            contacto.save()

            return redirect("/contacto/?valido")


    return render(request, "blogsetup/contacto.html", {"categorias":categorias, "formulario":formulario_contacto})

class RegistroBlog(View):
    

    def get(self,request):
        categorias=Categoria.objects.all()
        form = CustomUserCreationForm()

        return render(request, "blogsetup/registro.html", {"form":form, "categorias":categorias})

    
    def post(self,request):
        categorias=Categoria.objects.all()
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return redirect('index')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "blogsetup/registro.html", {"form":form, "categorias":categorias})
        
def ingresar(request):
    categorias=Categoria.objects.all()
    form=AuthenticationForm()

    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')

            else:
                messages.error(request, "Usuario Invalido")

        else:
            messages.error(request, "Informacion incorrecta")

    return render(request, "blogsetup/ingresar.html", {"categorias":categorias, "form":form})

def cerrarsesion(request):
    logout(request)
    return redirect('index')

@login_required
def crearpost(request):
    data={'form':ContenidoForms()}

    if request.method=="POST":
        formulario = ContenidoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario


    return render(request, "paginas/crearpost.html", data)

@login_required
def listado(request):
    contenidos = reversed(Contenido.objects.all())

    return render(request, "paginas/listado.html", {"contenidos":contenidos})



@login_required
def editar(request, contenido_id):

    contenido = get_object_or_404(Contenido, id=contenido_id)

    data = {
        'form':ContenidoForms(instance=contenido)
    }

    if request.method=="POST":
        formulario = ContenidoForms(data=request.POST, instance=contenido, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, "paginas/modificar.html", data)

@login_required
def eliminar(request, contenido_id):
    contenido = get_object_or_404(Contenido, id=contenido_id)
    contenido.delete()

    return redirect(to="listado")
