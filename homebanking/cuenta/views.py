from django.shortcuts import render, HttpResponse


# Create your views here.


def cuenta(request):
    return render(request, "cuenta/cuenta.html")
