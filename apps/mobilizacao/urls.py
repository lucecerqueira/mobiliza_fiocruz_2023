from django.urls import path
from .views import TarefaListView

urlpatterns = [
    path("", TarefaListView.as_view(), name="tarefas_lista"),
]
