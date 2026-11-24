from django.contrib import admin
from .models import PerfilParticipante
@admin.register(PerfilParticipante)
class PerfilParticipanteAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nome_publico", "aceita_comunicacoes", "criado_em")
    list_filter = ("aceita_comunicacoes",)
    search_fields = ("usuario__username", "nome_publico", "usuario__email")
