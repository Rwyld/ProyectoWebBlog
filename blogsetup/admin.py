from django.contrib import admin
from .models import *

# Register your models here.

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'autor', 'fecha')
    readonly_fields = ('created', 'update')

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contraseña', 'email')
    readonly_fields = ('created', 'update')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asunto', 'email', 'mensaje')
    readonly_fields = ('created', 'update')

class CategAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(DiseñoWeb)
admin.site.register(Categoria, CategAdmin)