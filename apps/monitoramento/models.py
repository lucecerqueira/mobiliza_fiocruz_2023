from django.db import models

class InteracaoInstitucional(models.Model):
    instituicao = models.CharField(max_length=150)
    assunto = models.CharField(max_length=220)
    descricao = models.TextField()
    data = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=80, default="Aguardando resposta")
    fonte = models.URLField(blank=True)
    resposta = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instituicao}: {self.assunto}"

class Indicador(models.Model):
    nome = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    unidade = models.CharField(max_length=40, blank=True)
    periodo = models.DateField()
    origem = models.URLField(blank=True)
    observacao = models.TextField(blank=True)

    class Meta:
        ordering = ["-periodo"]

    def __str__(self):
        return f"{self.nome} ({self.periodo})"
