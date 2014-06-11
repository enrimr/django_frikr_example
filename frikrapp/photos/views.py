# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Photo, VISIBILITY_PUBLIC
from django.http.response import HttpResponseNotFound
from django.contrib.auth import authenticate, login

def home(request): # En Django los controladores siempre reciben un objeto HttpRequest
    """
    Se ejecuta en /helloworld
    :param request: objeto request
    :return: objeto response
    """

    photo_list = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')[:3]

    context = {
        'photos': photo_list
    }

    return render(request, 'photos/index.html', context)

def photo_detail(request, pk):
    """
    Muestra el detalle de una foto
    :param request: objeto request
    :param pk: primary key de la foto
    :return: objeto response
    """
    possible_photos = Photo.objects.filter(pk=pk, visibility=VISIBILITY_PUBLIC)

    if len(possible_photos) == 0:
        return HttpResponseNotFound('No existe la foto seleccionada')
    else:
        context = {
            'photo': possible_photos[0]
        }
        return render(request,'photos/photo_detail.html', context)

def user_login(request):
    """
    Gestiona el login de un usuario
    :param request: objeto request
    :return: objeto response
    """
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('user_username')
        password = request.POST.get('user_password')
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append('Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                login(request, user) # crea la sesión de usuario
                return redirect('/')
            else:
                error_messages.append('El usuario no está activo')

    context = {
        'errors' : error_messages
    }

    return render(request, 'photos/login.html', context)