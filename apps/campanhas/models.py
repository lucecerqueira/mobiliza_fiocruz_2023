from django.db import models

class Campanha(models.Model):
    STATUS = [("rascunho", "Rascunho"), ("ativa", "Ativa"), ("encerrada", "Encerrada")]
    titulo = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    objetivo = models.TextField()
    inicio = models.DateField(null=True, blank=True)
    encerramento = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS, default="rascunho")
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
