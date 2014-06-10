from django.db import models

LICENSES = (
    ('RIG', 'Copyright'),
    ('LEF', 'Copyleft'),
    ('CC', 'CreativeCommons')
)
class Photo(models.Model):

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True) # opcional
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)

    def __unicode__(self):
        return self.name # para mostrar el campo name como nombre en la tabla