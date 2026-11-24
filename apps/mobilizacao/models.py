from django.conf import settings
from django.db import models

class Tarefa(models.Model):
    TIPOS = [("compartilhar", "Compartilhar material"), ("revisar", "Revisar informação"), ("articular", "Articulação institucional"), ("sugerir", "Sugerir pauta")]
    STATUS = [("aberta", "Aberta"), ("andamento", "Em andamento"), ("concluida", "Concluída")]
    titulo = models.CharField(max_length=180)
    descricao = models.TextField()
    tipo = models.CharField(max_length=15, choices=TIPOS)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS, default="aberta")
    voluntaria = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
