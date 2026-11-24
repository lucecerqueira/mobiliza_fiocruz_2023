from django.urls import path
from .views import PublicacaoListView

urlpatterns = [
    path("", PublicacaoListView.as_view(), name="publicacoes_lista"),
]
