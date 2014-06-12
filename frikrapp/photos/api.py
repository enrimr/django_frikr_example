# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from serializers import UserSerializer, PhotoSerializer, PhotoListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView # en lugar de importar View de django, importamos APIView de rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import status
from models import Photo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all() # recuperamos todos los usuarios de la base de datos
        serializer = UserSerializer(users, many=True) # transforma cada usuario de la lista en una lista de diccionarios
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid(): # los serializer funcionan como los djangoforms, así que hay que validarlo
            serializer.save()     # guardamos en la base de datos el nuevo usuario
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhotoListAPI(ListCreateAPIView):
    """
    Implementa el API de listado (GET) y creación (POST) de fotos
    (Sí, enserio)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Implementa el API de detalle (GET), actualización (PUT) y borrado (DELETE)
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
