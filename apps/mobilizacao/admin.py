from django.contrib import admin
from .models import Tarefa
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "status", "responsavel", "voluntaria")
    list_filter = ("tipo", "status", "voluntaria")
