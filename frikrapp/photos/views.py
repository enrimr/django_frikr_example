from django.shortcuts import render
from models import Photo, VISIBILITY_PUBLIC
from django.http.response import HttpResponseNotFound

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