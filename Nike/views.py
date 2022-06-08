from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from Nike.models import indumentarias,calzados,accesorios
from Nike.forms import Indumentarias_form, Calzados_form, Accesorios_form

#--------------------------------------Parte de Indumentarias--------------------------------------------------------------
def indumentaria_view(request):
    print(request.method)
    productos = indumentarias.objects.all()
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def crear_productos_indumentarias(request):
    if request.method == 'GET':
        form = Indumentarias_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Indumentarias_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_indumentaria = indumentarias.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
                cod_estacion = form.cleaned_data['cod_estacion'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
            )
            context ={'nuevo_indumentaria':nuevo_indumentaria}
        return render(request, 'create_product.html', context=context)

def buscar_productos_indumentarias(request):
    print(request.GET)
    products = indumentarias.objects.filter(name__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context = context)

def Remeras(request):
    print(request.method)
    productos = indumentarias.objects.filter(cod_categoria = 1)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Pantalones(request):
    print(request.method)
    productos = indumentarias.objects.filter(cod_categoria = 2)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Camperas(request):
    print(request.method)
    productos = indumentarias.objects.filter(cod_categoria = 3)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Buzos(request):
    print(request.method)
    productos = indumentarias.objects.filter(cod_categoria = 4)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)
#--------------------------------------Parte de Calzados--------------------------------------------------------------
def calzado_view(request):
    print(request.method)
    calzado = calzados.objects.all()
    context = {'calzado':calzado}
    return render(request, 'calzado.html', context=context)

def crear_productos_calzados(request):
    if request.method == 'GET':
        form = Calzados_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Calzados_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_calzado = calzados.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
            )
            context ={'nuevo_calzado':nuevo_calzado}
        return render(request, 'create_product.html', context=context)

def buscar_productos_calzados(request):
    print(request.GET)
    calzado = calzados.objects.filter(name__contains = request.GET['search'])
    context = {'calzado':calzado}
    return render(request, 'search_product.html', context = context)

def ZapatillaDeportiva(request):
    print(request.method)
    productos = calzados.objects.filter(cod_categoria = 1)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def ZapatillaComunes(request):
    print(request.method)
    productos = calzados.objects.filter(cod_categoria = 2)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Botines(request):
    print(request.method)
    productos = calzados.objects.filter(cod_categoria = 3)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Ojotas(request):
    print(request.method)
    productos = calzados.objects.filter(cod_categoria = 4)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)
#--------------------------------------Parte de Accesorios--------------------------------------------------------------
def accesorio_view(request):
    print(request.method)
    accesorio = accesorios.objects.all()
    context = {'accesorio':accesorio}
    return render(request, 'accesorio.html', context=context)

def crear_productos_accesorios(request):
    if request.method == 'GET':
        form = Accesorios_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Accesorios_form(request.POST,files=request.FILES)
        if form.is_valid():
            nuevo_accesorio = accesorios.objects.create(
                codigo_barra = form.cleaned_data['codigo_barra'],
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                color = form.cleaned_data['color'],
                cod_categoria = form.cleaned_data['cod_categoria'],
                imagen = form.cleaned_data['imagen'],
            )
            context ={'nuevo_accesorio':nuevo_accesorio}
        return render(request, 'create_product.html', context=context)

def buscar_productos_accesorios(request):
    print(request.GET)
    accesorio = accesorios.objects.filter(name__contains = request.GET['search'])
    context = {'accesorio':accesorio}
    return render(request, 'search_product.html', context = context)

def Pelota(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 1)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Pulseras(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 2)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Cantiplora(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 3)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Anteojos(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 4)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Muñequeras(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 5)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Bolsos_Mochilas(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 6)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Llaveros(request):
    print(request.method)
    productos = accesorios.objects.filter(cod_categoria = 7)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

