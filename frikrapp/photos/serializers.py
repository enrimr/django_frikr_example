# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password # para poder encriptar el password nuevo que generamos
from django.conf import settings

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

    def validate(self, attrs):
        existent_users = User.objects.filter(username=attrs.get('username'))
        if len(existent_users) > 0:
            raise serializers.ValidationError(u"Ya existe el usuario: " + attrs.get('username'))
        return attrs # to_do ha ido bien

        # TODO
        # hay que arreglar el hecho de que ya no nos deje crear usuarios nuevos: currrandonos el metodo put y haciendo
        #  la validación a mano, o definiendo un serializer UserUpdateSerializer que herede de UserSerializer y
        # hacer otro validate()

class UserUpdateSerializer(UserSerializer):
    """
    Serializador que se usa al hacer PUT de un usuario y que hereda de UserSerializer.
    La justificación de separar este serializador y no el otro, es porque en UserSerializer comprobamos que el usuario
    no exista ya, lo que nos puede dar error en el PUT
    """
    def validate(self, attrs):
        return attrs


# Las importaciones no tienen por qué ser al principio del fichero
from models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo

class PhotoListSerializer(PhotoSerializer):

    class Meta(PhotoSerializer.Meta):

        fields = ('id', 'owner', 'name')