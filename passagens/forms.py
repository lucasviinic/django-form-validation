from django import forms
from django.forms.forms import Form

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida')
    data_volta = forms.DateField(label='Volta')