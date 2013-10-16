from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.admin import site
admin.autodiscover()

from common.models import *
site.register(Persona)
site.register(Auto)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitio.views.home', name='home'),
    # url(r'^sitio/', include('sitio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
