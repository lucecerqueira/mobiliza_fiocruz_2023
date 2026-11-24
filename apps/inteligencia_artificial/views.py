import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from apps.publicacoes.models import Publicacao
from .forms import ImpulsionamentoForm
from .models import RegistroImpulsionamento
from .services import gerar_lote_impulsionamento


@login_required
def gerar(request):
    variacoes = []
    post_url = "https://www.instagram.com/p/DgFYs8wFmlV/"
    hashtag_atual = "#ConvocaFiocruz"

    if request.method == "POST":
        form = ImpulsionamentoForm(request.POST)
        if form.is_valid():
            post_url = form.cleaned_data["post_url"]
            hashtag_atual = form.cleaned_data["hashtag"] or "#ConvocaFiocruz"
            variacoes = gerar_lote_impulsionamento(
                texto_base=form.cleaned_data["texto_base"],
                quantidade=int(form.cleaned_data["quantidade"]),
                arroba_custom=form.cleaned_data["arroba_alvo"],
                hashtag_custom=hashtag_atual,
            )

            if request.POST.get("registrar_post") == "1":
                Publicacao.objects.get_or_create(
                    url=post_url,
                    defaults={
                        "titulo": f"Post Alvo - {hashtag_atual}",
                        "instituicao": "fiocruz",
                        "plataforma": "instagram",
                        "texto_publicacao": form.cleaned_data["texto_base"],
                        "relevante": True,
                    },
                )
                messages.success(
                    request,
                    f"{len(variacoes)} variações geradas e post alvo registrado em Publicações!",
                )
            else:
                messages.success(request, f"{len(variacoes)} variações prontas para impulsionamento!")
    else:
        form = ImpulsionamentoForm()

    # Auditoria em tempo real do banco de dados
    total_copiados = RegistroImpulsionamento.objects.count()
    total_abertos = RegistroImpulsionamento.objects.filter(abriu_post=True).count()
    ultimos_registros = RegistroImpulsionamento.objects.select_related("usuario")[:15]
    ranking_usuarios = (
        RegistroImpulsionamento.objects.values("usuario__username")
        .annotate(total=Count("id"))
        .order_by("-total")[:10]
    )

    return render(
        request,
        "ia/gerar.html",
        {
            "form": form,
            "variacoes": variacoes,
            "post_url": post_url,
            "hashtag_atual": hashtag_atual,
            "total_copiados": total_copiados,
            "total_abertos": total_abertos,
            "ultimos_registros": ultimos_registros,
            "ranking_usuarios": ranking_usuarios,
        },
    )


@login_required
@require_POST
def registrar_clique(request):
    try:
        dados = json.loads(request.body)
        RegistroImpulsionamento.objects.create(
            usuario=request.user,
            post_url=dados.get("post_url", ""),
            hashtag=dados.get("hashtag", ""),
            texto_utilizado=dados.get("texto", ""),
            abriu_post=bool(dados.get("abriu_post", False)),
        )
        return JsonResponse(
            {
                "status": "ok",
                "total_copiados": RegistroImpulsionamento.objects.count(),
                "total_abertos": RegistroImpulsionamento.objects.filter(abriu_post=True).count(),
            }
        )
    except Exception as exc:
        return JsonResponse({"status": "erro", "detalhe": str(exc)}, status=400)