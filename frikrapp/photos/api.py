# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView # en lugar de importar View de django, importamos APIView de rest_framework

class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all() # recuperamos todos los usuarios de la base de datos
        serializer = UserSerializer(users, many=True) # transforma cada usuario de la lista en una lista de diccionarios
        return Response(serializer.data)
