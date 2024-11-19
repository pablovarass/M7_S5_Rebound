from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import FabricaForm, ProductoForm
from .models import Producto, Fabrica

# Vistas de Fábricas
@login_required
def listar_fabricas(request):
    fabricas = Fabrica.objects.all()
    return render(request, 'listar_fabricas.html', {'fabricas': fabricas})

@login_required
def crear_fabrica(request):
    if request.method == 'POST':
        form = FabricaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Fábrica "{form.cleaned_data.get("nombre")}" creada correctamente.')
            return redirect('listar_fabricas')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = FabricaForm()
    return render(request, 'crear_fabrica.html', {'form': form})

@login_required
def editar_fabrica(request, fabrica_id):
    fabrica = get_object_or_404(Fabrica, id=fabrica_id)
    if request.method == 'POST':
        form = FabricaForm(request.POST, instance=fabrica)
        if form.is_valid():
            form.save()
            messages.success(request, f'Fábrica "{fabrica.nombre}" actualizada correctamente.')
            return redirect('listar_fabricas')
    else:
        form = FabricaForm(instance=fabrica)
    return render(request, 'editar_fabrica.html', {'form': form})

@login_required
def eliminar_fabrica(request, fabrica_id):
    fabrica = get_object_or_404(Fabrica, id=fabrica_id)
    if request.method == 'POST':
        fabrica.delete()
        messages.success(request, f'Fábrica "{fabrica.nombre}" eliminada correctamente.')
        return redirect('listar_fabricas')
    return render(request, 'eliminar_fabrica.html', {'fabrica': fabrica})

# Vistas de Productos
@login_required
def listar_productos(request):
    productos = Producto.objects.select_related('fabrica').all()
    return render(request, 'listar_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado correctamente.')
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, f'Producto "{producto.nombre}" eliminado correctamente.')
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

# Vistas de Usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('listar_productos')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'login.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')

# Página de inicio
class IndexPageView(TemplateView):
    template_name = 'index.html'

def home_page(request):
    return render(request, 'index.html')

