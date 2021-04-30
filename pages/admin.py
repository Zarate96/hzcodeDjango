from django.contrib import admin
from .models import Mensajes, Demo

# Register your models here.
class MensajestAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'asunto', 'is_answered')
    search_fields = ('nombre', 'email')
    list_per_page = 10

admin.site.register(Mensajes, MensajestAdmin)

class DemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'url_pag')
    search_fields = ('nombre','url_pag',)
    list_per_page = 10

admin.site.register(Demo, DemoAdmin)
