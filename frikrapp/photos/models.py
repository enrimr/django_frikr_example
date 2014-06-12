# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError

DEFAULT_LICENSES = (
    ('RIG', 'Copyright'),
    ('LEF', 'Copyleft'),
    ('CC', 'CreativeCommons')
)

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Publica'),
    (VISIBILITY_PRIVATE, 'Privada')
)

# Permite que BADWORDS se pueda reescribir desde el settings.py
BADWORDS = getattr(settings, 'BADWORDS', ())

class Photo(models.Model):

    owner = models.ForeignKey(User) # Clave foranea User
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True) # opcional
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY)

    def __unicode__(self):
        return self.name # para mostrar el campo name como nombre en la tabla

    def clean(self):
        for badword in BADWORDS:
            if badword.lower() in self.description.lower():
                raise ValidationError(badword + u' no está permitido')