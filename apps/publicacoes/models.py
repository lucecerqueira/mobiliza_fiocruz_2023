from django.db import models

class Publicacao(models.Model):
    PLATAFORMAS = [("instagram", "Instagram"), ("tiktok", "TikTok"), ("site", "Site institucional"), ("outra", "Outra")]
    INSTITUICOES = [("fiocruz", "Fiocruz"), ("presidencia", "Presidência da República"), ("saude", "Ministério da Saúde"), ("mgi", "MGI"), ("congresso", "Congresso Nacional"), ("outra", "Outra")]
    titulo = models.CharField(max_length=220)
    url = models.URLField(max_length=500)
    instituicao = models.CharField(max_length=20, choices=INSTITUICOES)
    plataforma = models.CharField(max_length=15, choices=PLATAFORMAS, default="instagram")
    texto_publicacao = models.TextField(blank=True)
    resumo = models.TextField(blank=True)
    data_publicacao = models.DateTimeField(null=True, blank=True)
    relevante = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
