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

    def post(self, request):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid(): # los serializer funcionan como los djangoforms, así que hay que validarlo
            serializer.save()     # guardamos en la base de datos el nuevo usuario
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)