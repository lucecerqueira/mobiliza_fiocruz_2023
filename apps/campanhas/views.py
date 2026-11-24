from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.campanhas.models import Campanha
from apps.publicacoes.models import Publicacao
from apps.conteudos.models import Conteudo
from apps.usuarios.models import PerfilParticipante

def dashboard(request):
    contexto = {
        "campanhas": Campanha.objects.all()[:5],
        "total_campanhas": Campanha.objects.count(),
        "total_publicacoes": Publicacao.objects.count(),
        "total_conteudos": Conteudo.objects.count(),
        "total_participantes": PerfilParticipante.objects.filter(aceita_comunicacoes=True).count(),
    }
    return render(request, "dashboard/index.html", contexto)
