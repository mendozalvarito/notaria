from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, mixins

class InicioView(View):
    mensaje = None
    plantilla = 'nucleo/inicio.html'
    contexto = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('nucleo:escritorio')
        return render(request, self.plantilla, self.contexto)

    def post(self, request, *args, **kwargs):
        user = authenticate(
            username = request.POST['usuario'], 
            password = request.POST['contraseña']
        )
        if user is not None:
            login(request, user)
            return redirect('nucleo:escritorio')
        else:
            self.mensaje = "Usuario y Contraseña incorrectos"
            self.contexto = {'mensaje':self.mensaje}
        return render(request, self.plantilla, self.contexto)

class EscritorioView(mixins.LoginRequiredMixin,View):
    mensaje = None
    plantilla = 'nucleo/escritorio.html'
    contexto = {}
    login_url = 'inicio'

    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.contexto)