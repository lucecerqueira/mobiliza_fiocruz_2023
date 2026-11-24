from django.contrib import admin
from .models import Campanha
@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "status", "inicio", "encerramento")
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("titulo",)}
