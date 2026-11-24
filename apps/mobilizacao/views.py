from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Tarefa

class TarefaListView(ListView):
    model = Tarefa
    template_name = "mobilizacao/lista.html"
    context_object_name = "tarefas"
    def get_queryset(self):
        return Tarefa.objects.filter(voluntaria=True).order_by("status", "-criada_em")
