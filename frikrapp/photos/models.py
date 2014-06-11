from django.db import models
from django.contrib.auth.models import User

LICENSES = (
    ('RIG', 'Copyright'),
    ('LEF', 'Copyleft'),
    ('CC', 'CreativeCommons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Publica'),
    (VISIBILITY_PRIVATE, 'Privada')
)

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