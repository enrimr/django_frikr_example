from django.contrib import admin
from models import Photo

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'license', 'visibility', 'owner_name')
    list_filter = ('license', 'visibility')

    def owner_name(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name

    owner_name.short_description = 'Propietario'
    owner_name.admin_order_field = 'owner'

admin.site.register(Photo, PhotoAdmin)