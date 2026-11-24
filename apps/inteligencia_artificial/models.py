from django.conf import settings
from django.db import models


class RegistroImpulsionamento(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="disparos_impulsionamento",
    )
    post_url = models.URLField(max_length=500)
    hashtag = models.CharField(max_length=80, blank=True)
    texto_utilizado = models.TextField()
    abriu_post = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        nome = self.usuario.username if self.usuario else "Anônimo"
        return f"{nome} - {self.hashtag} ({self.criado_em:%d/%m %H:%M})"