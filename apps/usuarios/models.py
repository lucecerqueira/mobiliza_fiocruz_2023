from django.conf import settings
from django.db import models

class PerfilParticipante(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil_participante")
    nome_publico = models.CharField(max_length=120, blank=True)
    aceita_comunicacoes = models.BooleanField(default=False)
    consentimento_em = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_publico or self.usuario.username
