from django import forms

from .models import Local, Embalagem


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'tipo']

class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem
        fields = ['name', 'sigla']
