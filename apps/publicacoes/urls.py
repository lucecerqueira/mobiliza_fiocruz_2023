from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PublicacaoListView
urlpatterns = [path("", login_required(PublicacaoListView.as_view()), name="publicacoes_lista")]
