from django.shortcuts import render

# Create your views here.


from .models import Cliente


def cliente(request):
    return render(request, "cliente/cliente.html")


def cliente_list(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'cliente/cliente.html', {'clientes': clientes})
