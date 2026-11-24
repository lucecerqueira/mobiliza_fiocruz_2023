from django.urls import path
from django.views.generic import ListView
from .models import Campanha

urlpatterns = [
    path("", ListView.as_view(model=Campanha, template_name="campanhas/lista.html"), name="campanhas_lista"),
]
