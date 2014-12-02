from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('home.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^empresa', 'empresa', name='empresa'),
    url(r'^diseno_web', 'disenoweb', name='disenoweb'),
    url(r'^marketing', 'marketing', name='marketing'),
    url(r'^contacto', 'contacto', name='contacto'),

    
)