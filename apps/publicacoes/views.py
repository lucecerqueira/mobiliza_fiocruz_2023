from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Publicacao

class PublicacaoListView(ListView):
    model = Publicacao
    template_name = "publicacoes/lista.html"
    context_object_name = "publicacoes"
    paginate_by = 20

    def get_queryset(self):
        return Publicacao.objects.filter(relevante=True)
