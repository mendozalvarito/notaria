from django.urls import path
from .vistas import pais

app_name = 'cliente'

urlpatterns = [
    path("listar-pais/", pais.PaisListView.as_view(), name="listar-pais"),
    path("ver-pais/<int:pk>/", pais.PaisDetailView.as_view(), name="ver-pais"),
    path("crear-pais/<int:pk>/", pais.PaisDetailView.as_view(), name="crear-pais"),
    path("modificar-pais/<int:pk>/", pais.PaisUpdateView.as_view(), name="modificar-pais"),
    path("eliminar-pais/<int:pk>/", pais.PaisDetailView.as_view(), name="eliminar-pais"),
]