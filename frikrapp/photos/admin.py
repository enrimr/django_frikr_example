from django.contrib import admin
from models import Photo

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'license', 'visibility', 'owner_name')

    def owner_name(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name

admin.site.register(Photo, PhotoAdmin)