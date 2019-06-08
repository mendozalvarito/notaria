from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout

# Create your views here.

@login_required(login_url = 'inicio')
def cerrar(request):
    logout(request)
    return redirect('inicio')

def restablecer(request):
    return render(request,"nucleo/restablecer.html")

def registrar(request):
    return render(request,"nucleo/registrar.html")