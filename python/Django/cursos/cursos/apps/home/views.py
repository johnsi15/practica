from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from cursos.apps.productos.forms import AgregarForm, ActulizarForm
from cursos.apps.productos.models import Producto
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required #esto es para evitar problemas con el de agregar

def index(request):
	#si queremos mostrar solo disponibles
	producto = Producto.objects.filter(disponible= True).order_by('-id')[:10]#manejamos el orden y la cantidad
	#producto = Producto.objects.all()
	ctx = {'producto':producto}
	return render_to_response('home/index.html', ctx ,context_instance = RequestContext(request))

@login_required
def agregar(request):
	form = AgregarForm
    #con todo este codigo manmos los datos a la base de datos para registrar
	if request.method == "POST":
		form = AgregarForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			categoria = form.cleaned_data['categoria'].id

			p = Producto()
			p.nombre = nombre
			p.descripcion = descripcion
			p.categoria_id = categoria
			p.usuario_id = request.user.id
			p.save()
			return HttpResponseRedirect('/')

	ctx = {'form': form}
	return render_to_response('home/agregar.html', ctx, context_instance=RequestContext(request))

@login_required
def actualizar(request, idp):
	get_object_or_404(Producto, id=idp)
	p = Producto.objects.get(id=idp)#con esto mandamos a traer uno solo es como Limit en query
	form = ActulizarForm(instance=p)#llenamos el formulario con los datos que estamos pasando 
	if request.method == "POST":
		form = ActulizarForm(request.POST, instance=p)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	ctx = {'form':form}
	return render_to_response('home/actualizar.html', ctx, context_instance=RequestContext(request))
