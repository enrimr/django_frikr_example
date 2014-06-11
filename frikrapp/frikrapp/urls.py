# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from photos import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Web URLs
    url(r'^$', views.HomeView.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDetailView.as_view()),
    # photo_detail va a recibir un parametro llamado pk
    # que es un numero de 1 o mas cifras entre 0-9

    url(r'^login$', 'photos.views.user_login'),
    url(r'^logout$', 'photos.views.user_logout'),
    url(r'^profile$', 'photos.views.user_profile'),
    url(r'^create$', 'photos.views.create_photo')
)
