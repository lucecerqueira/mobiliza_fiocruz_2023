from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ConteudoListView
urlpatterns = [path("", login_required(ConteudoListView.as_view()), name="conteudos_lista")]
