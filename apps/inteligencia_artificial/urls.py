from django.urls import path
from .views import gerar, registrar_clique

urlpatterns = [
    path("gerar/", gerar, name="ia_gerar"),
    path("registrar-clique/", registrar_clique, name="ia_registrar_clique"),
]