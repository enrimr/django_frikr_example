from django.shortcuts import render
from models import Photo, VISIBILITY_PUBLIC

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