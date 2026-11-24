from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import PerfilParticipante

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome_publico = forms.CharField(max_length=120, required=False, label="Nome público (opcional)")
    aceita_comunicacoes = forms.BooleanField(required=True, label="Concordo em receber comunicações do movimento e li o aviso de privacidade.")

    class Meta:
        model = User
        fields = ("username", "email", "nome_publico", "password1", "password2", "aceita_comunicacoes")

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]
        if commit:
            usuario.save()
            PerfilParticipante.objects.create(
                usuario=usuario,
                nome_publico=self.cleaned_data.get("nome_publico", ""),
                aceita_comunicacoes=True,
                consentimento_em=timezone.now(),
            )
        return usuario
