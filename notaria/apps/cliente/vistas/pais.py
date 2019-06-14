from ..models import Pais
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from ..forms import PaisForm

class PaisListView(LoginRequiredMixin, ListView):
    template_name = 'crud/listar.html'
    model = Pais
    context_object_name = 'lista'
    login_url = '/'
    redirect_field_name = 'no_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulos'] = ['#' , 'Pais' , 'Codigo']
        context['campos'] = ['nombre' , 'codigo']
        context['titulo'] = 'Pais'
        context['urls'] = {'ver' : 'cliente:ver-pais', 'modificar' : 'cliente:modificar-pais',
                'crear' : 'cliente:crear-pais', 'eliminar':'cliente:eliminar-pais'}
        return context

class PaisDetailView(LoginRequiredMixin ,DetailView):
    model = Pais
    template_name = 'crud/ver.html'
    login_url = '/'
    redirect_field_name = 'no_login'

class PaisUpdateView(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'crud/crear.html'
    success_url = reverse_lazy('cliente:listar-pais')
    
class PaisCreateView(CreateView):
    form_class = PaisForm
    template_name = 'crud/crear.html'
    success_url = reverse_lazy('cliente:listar-pais')

class PaisDeleteView(DeleteView):
    model = Pais
    success_url = reverse_lazy('cliente:listar-pais')