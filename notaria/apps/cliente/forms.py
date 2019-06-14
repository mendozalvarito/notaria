from django.forms import ModelForm
from .models import Pais

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"