# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Web URLs
    url(r'^$', 'photos.views.home'),
    url(r'^photos/(?P<pk>[0-9]+)$', 'photos.views.photo_detail'),
    # photo_detail va a recibir un parametro llamado pk
    # que es un numero de 1 o mas cifras entre 0-9

    url(r'^login$', 'photos.views.user_login'),
    url(r'^logout$', 'photos.views.user_logout')
)
