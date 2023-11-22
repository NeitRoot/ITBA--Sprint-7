from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "itbank/inicio.html") 

def sesion(request):
    return render(request, "itbank/sesion.html") 