from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'principal.views.index'), #locahost:8000
	url(r'^productos/$', 'principal.views.productos')
)
