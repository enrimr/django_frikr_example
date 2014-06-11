from django.contrib import admin
from models import Photo

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'license', 'visibility', 'owner')

admin.site.register(Photo, PhotoAdmin)