from django.contrib import admin
from .models import Tema, Conteudo
admin.site.register(Tema)
@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "tema", "status", "criado_em")
    list_filter = ("tipo", "status", "tema")
    search_fields = ("titulo", "texto")
