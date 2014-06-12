# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from serializers import UserSerializer, PhotoSerializer, PhotoListSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView # en lugar de importar View de django, importamos APIView de rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import status
from models import Photo, VISIBILITY_PUBLIC
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions import UserPermission
from django.db.models import Q

class UserListAPI(APIView):

    permission_classes = (UserPermission,)

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

    permission_classes = (UserPermission,)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            serializer = UserUpdateSerializer(user, data=request.DATA)  # Usamos el serializador UserUpdateSerializer que
                                                                        # hereda de UserSerializer, para que podamos hacer
                                                                        # otro tipo de validación y que nos deje actualizar
                                                                        # el usuario

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PhotoAPIQueryset:

    def get_queryset(self):
        """
        Devuelve un queryset en función de varios criterios
        """

        # Si es superusuario, devuelve la lista entera
        if self.request.user.is_superuser:
            return Photo.objects.all()

        # Si el usuario no es superuser pero está autenticado, devolvemos todas las fotos públicas y todas sus fotos
        elif self.request.user.is_authenticated():
            return Photo.objects.filter(Q(visibility=VISIBILITY_PUBLIC) | Q(owner=self.request.user))

        # En cualquier otro caso, devuelvo solamente las fotos públicas
        else:
            return Photo.objects.filter(visibility=VISIBILITY_PUBLIC)

class PhotoListAPI(PhotoAPIQueryset, ListCreateAPIView): # llama al metod de la primera clase que hereda
    """
    Implementa el API de listado (GET) y creación (POST) de fotos
    (Sí, enserio)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        # Si estamos haciendo un POST devolvemos el serializador PhotoSerializer (que tiene todos los campos)
        # y si es un GET, usamos el PhotoListSerializer que solo tiene los 3 campos que queremos
        return PhotoSerializer if self.request.method == "POST" else self.serializer_class

    def pre_save(self, obj):
        """
        Asigna la autoría de la foto al usuario autenticado al crearla
        """
        obj.owner = self.request.user


class PhotoDetailAPI(PhotoAPIQueryset, RetrieveUpdateDestroyAPIView):
    """
    Implementa el API de detalle (GET), actualización (PUT) y borrado (DELETE)
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
