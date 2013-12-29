from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'), # 127.0.0.1:8000 - localhost:8000
    url(r'^envio/$', 'principal.views.envio'),
    url(r'^productos/$', 'principal.views.productos')
)
