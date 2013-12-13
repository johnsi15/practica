# Create your views here.
from blog.models import Entrada
from django.http import HttpResponse

def index(request):
	# return HttpResponse("Bienvenidos al Blog Jandrey")
	verEntradas = Entrada.objects.all().order_by('fecha')
	salida = ', '.join([p.titulo for p in verEntradas])
	return HttpResponse(salida)