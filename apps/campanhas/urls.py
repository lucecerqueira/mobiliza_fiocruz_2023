from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Campanha

urlpatterns = [
    path("", login_required(ListView.as_view(model=Campanha, template_name="campanhas/lista.html")), name="campanhas_lista"),
]
