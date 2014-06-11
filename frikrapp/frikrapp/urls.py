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

    url(r'^login$', views.UserLoginView.as_view()),
    url(r'^logout$', views.UserLogoutView.as_view()),
    url(r'^profile$', views.UserProfileView.as_view()),
    url(r'^create$', 'photos.views.create_photo')
)
