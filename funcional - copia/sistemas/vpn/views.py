from django.shortcuts import render, redirect
import subprocess
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'paginas/usuarios.html', {'usuarios':usuarios})

def crear(request):
    formulario =UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'crear.html', {'formulario': formulario})

def editar(request, id):
    usuario =  Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        
        return redirect('usuarios')
    return render(request, 'editar.html', {'formulario': formulario})

def mk(request):
    subprocess.call(['python', 'C:/Users/mayra.moises/OneDrive - SA AVENUE/Escritorio/funcional/sistemas/vpn/mk.py'])
    return render (request,'paginas/usuarios.html')

def eliminar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')

def documentacion(request):
    return render(request, 'paginas/documentacion.html')

def parse_form(content):
    import lxml.html
    tree = lxml.html.fromstring(content)
    return dict(tree.forms[0].fields)


