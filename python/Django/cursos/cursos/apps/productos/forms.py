# -o- coding: utf-8 -o- 
#mostramos acentos
from django import forms
from django.forms import ModelForm
from cursos.apps.productos.models import Categoria, Producto

class AgregarForm(forms.Form):
	nombre = forms.CharField(widget = forms.TextInput(),required = True)
	categoria = forms.ModelChoiceField(queryset = Categoria.objects.all(), required= True, label="Categoría")#es un select llenando de un modelo #queryset = Categoria.objects.all() con esto selecionamos todo
	descripcion = forms.CharField(widget=forms.Textarea(), label="Descripción", required=True)

class ActulizarForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ('usuario','disponible')