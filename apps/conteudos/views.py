from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Conteudo

class ConteudoListView(ListView):
    model = Conteudo
    template_name = "conteudos/lista.html"
    context_object_name = "conteudos"
    paginate_by = 20

    def get_queryset(self):
        # Participantes veem apenas materiais aprovados pela coordenação.
        return Conteudo.objects.filter(status="aprovado")
