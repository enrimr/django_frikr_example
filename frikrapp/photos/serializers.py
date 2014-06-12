# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password # para poder encriptar el password nuevo que generamos

class UserSerializer(serializers.Serializer):

    id = serializers.Field() # Los campos field son campos de sólo lectura
    first_name = serializers.CharField() # no hace falta indicarle el max size ni nada
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        """
        Devuelve un objeto User en función de attr
        :param attrs: diccionario con datos
        :param instance: objeto user a actualizar
        :return: objeto User
        """
        if not instance:
            instance = User()

        instance.first_name = attrs.get('first_name')
        instance.last_name = attrs.get('last_name')
        instance.username = attrs.get('username')
        instance.email = attrs.get('email')

        # encriptamos password antes de asignar
        new_password = make_password(attrs.get('password'))
        instance.password = new_password

        return instance

from models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo