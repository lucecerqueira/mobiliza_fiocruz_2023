from django.contrib import admin
from .models import Publicacao
@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "instituicao", "plataforma", "relevante", "criada_em")
    list_filter = ("instituicao", "plataforma", "relevante")
    search_fields = ("titulo", "texto_publicacao", "resumo")
