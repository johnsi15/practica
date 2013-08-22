from django.conf.urls import patterns, include, url

urlpatterns = patterns('cursos.apps.home.views',
   	url(r'^$', 'index', name='index'),
	url(r'^agregar/', 'agregar', name ='agregar'),#segundo parametro la vista y el tercero el nombre
	url(r'^actualizar/(?P<idp>\w+)/$', 'actualizar', name = 'actualizar'),
)