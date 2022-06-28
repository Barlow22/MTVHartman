from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *


def inicio(request):
    
    return render(request, "AppMTV/inicio.html")


def clientes(request):

    
    if request.method == "POST":

        mi_formulario = Clientes_form(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            clientes = Clientes(nombre_fantasia=informacion['nombre_fantasia'], razon_social=informacion['razon_social'], cuit=informacion['cuit'], calle=informacion['calle'], altura=informacion['altura'], fecha_alta=informacion["fecha_alta"] )

            clientes.save()

            return render(request, "AppMTV/inicio.html")
    else:

        mi_formulario = Clientes_form()
    
    return render(request, "AppMTV/clientes.html", {"mi_formulario":mi_formulario})
    


def proveedores(request):
    

    if request.method == "POST":

        mi_formulario = Proveedores_form(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            clientes = Proveedores(nombre_fantasia=informacion['nombre_fantasia'], razon_social=informacion['razon_social'], cuit=informacion['cuit'], calle=informacion['calle'], altura=informacion['altura'], fecha_alta=informacion["fecha_alta"] )

            clientes.save()

            return render(request, "AppMTV/inicio.html")
    else:

        mi_formulario = Proveedores_form()
    
    return render(request, "AppMTV/proveedores.html", {"mi_formulario":mi_formulario})


def articulos(request):
    
    
    
    if request.method == "POST":

        mi_formulario = Articulos_form(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            clientes = Articulos(codigo=informacion['codigo'], nombre=informacion['nombre'], precio=informacion['precio'], stock=informacion['stock'])

            clientes.save()

            return render(request, "AppMTV/inicio.html")
    else:

        mi_formulario = Articulos_form()
    
    return render(request, "AppMTV/articulos.html", {"mi_formulario":mi_formulario})


def pagos(request):
    
    
    
    if request.method == "POST":

        mi_formulario = Pagos_form(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            clientes = Pagos(monto=informacion['monto'], forma_pago=informacion['forma_pago'], fecha_pago=informacion['fecha_pago'])

            clientes.save()

            return render(request, "AppMTV/inicio.html")
    else:

        mi_formulario = Pagos_form()
    
    return render(request, "AppMTV/pagos.html", {"mi_formulario":mi_formulario})



def buscar(request):

    if request.GET["nombre_fantasia"]:

        nombre_fantasia = request.GET["nombre_fantasia"]
        clientes = Clientes.objects.filter(nombre_fantasia__icontains=nombre_fantasia)

        return render(request, "AppMTV/clientes.html", {"clientes":clientes, "nombre_fantasia":nombre_fantasia})

    else:
        respuesta = "No envisate datos"

    return HttpResponse(respuesta)
