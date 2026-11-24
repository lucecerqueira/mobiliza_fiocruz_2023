from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import TarefaListView
urlpatterns = [path("", login_required(TarefaListView.as_view()), name="tarefas_lista")]
