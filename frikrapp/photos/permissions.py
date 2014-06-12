# -*- coding: utf-8 -*-
from rest_framework import permissions
from api import UserDetailAPI

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Define si se tiene permiso para realizas la acción
        :param request: objeto request
        :param view: Vista desde donde se ejecuta la acción
        :return: boolean
        """

        # Dejamos hacer un POST a todos el mundo
        if request.method == "POST":
            return True

        # Si es un superuser puede hacer un GET, PUT y DELETE si quiere
        elif request.user.is_superuser:
            return True

        # Si no es superuser le dejamos acceder solo al detalle
        elif isinstance(view, UserDetailAPI):
            return True

        # en cualquier otro caso, no permitimos realizar la acción
        else
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si se tiene permiso para hacer PUT o DELETE sobre obj
        Sólo tiene permiso si es propietario o es superuser
        :param request: objecto request
        :param view: vista desde donde se ejecuta
        :param obj: objecto sobre el que se ejecuta
        :return: boolean
        """
        if request.user.is_superuser or obj.owner == request.user:
            return True
        else:
            return False