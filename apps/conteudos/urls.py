from django.urls import path
from .views import ConteudoListView

urlpatterns = [
    path("", ConteudoListView.as_view(), name="conteudos_lista"),
]
