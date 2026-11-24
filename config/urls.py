from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from apps.campanhas.views import dashboard

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="/static/img/favicon.ico", permanent=False)),
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("contas/", include("apps.usuarios.urls")),
    path("campanhas/", include("apps.campanhas.urls")),
    path("publicacoes/", include("apps.publicacoes.urls")),
    path("conteudos/", include("apps.conteudos.urls")),
    path("mobilizacao/", include("apps.mobilizacao.urls")),
    path("ia/", include("apps.inteligencia_artificial.urls")),
]
