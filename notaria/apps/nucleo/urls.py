from django.urls import path
from . import views
from .vistas.nucleo import EscritorioView

app_name = 'nucleo'

urlpatterns = [
    path("restablecer/", views.restablecer, name="restablecer"),
    path("registrar/", views.registrar, name="registrar"),
    path("escritorio/", EscritorioView.as_view(), name="escritorio"),
]