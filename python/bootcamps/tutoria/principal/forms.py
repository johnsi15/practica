from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto