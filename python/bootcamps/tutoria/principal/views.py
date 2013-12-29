from django.shortcuts import render_to_response
from .forms import *
from .models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
	formulario = ProductoForm()
	ctx = { 'formulario':formulario }
	return render_to_response('index.html', ctx, context_instance=RequestContext(request))

def envio(request):
	if request.method == 'POST':
		formulario = ProductoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/productos')
		else:
			ctx = { 'formulario':formulario }
			return render_to_response('index.html', ctx, context_instance=RequestContext(request))

def productos(request):
	productos = Producto.objects.all()
	ctx = {'productos':productos}
	return render_to_response('productos.html', ctx)