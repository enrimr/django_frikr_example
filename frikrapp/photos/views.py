from django.shortcuts import render
#from django.http.response import HttpResponse
from models import Photo

def home(request): # En Django los controladores siempre reciben un objeto HttpRequest
    """
    Se ejecuta en /helloworld
    :param request: objeto request
    :return: objeto response
    """
    # html = '<strong>Hola mundo</strong>'
    #
    # return HttpResponse(html) # Los controladores siempre devuelven un HttpResponse

    photo_list = Photo.objects.all()

    context = {
        'photos' : photo_list
    }
    
    return render(request, 'photos/index.html', context)