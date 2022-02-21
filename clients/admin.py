from django.contrib import admin

from .models import Client

admin.site.register(Client)
# admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name','country','full_name')
