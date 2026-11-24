from django.conf import settings
from django.db import models

class Tema(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return self.nome

class Conteudo(models.Model):
    TIPOS = [("comentario", "Sugestão de manifestação"), ("legenda", "Legenda"), ("card", "Card"), ("roteiro", "Roteiro de vídeo"), ("documento", "Documento institucional"), ("perguntas", "Perguntas e respostas")]
    STATUS = [("rascunho", "Rascunho"), ("revisao", "Em revisão"), ("aprovado", "Aprovado"), ("arquivado", "Arquivado")]
    titulo = models.CharField(max_length=180)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    texto = models.TextField()
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS, default="rascunho")
    fonte = models.URLField(blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return self.titulo
