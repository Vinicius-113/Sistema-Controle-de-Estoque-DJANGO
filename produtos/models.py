from django.conf import settings
from django.db import models

# Create your models here.
class Produto(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="produtos",
        verbose_name="Usuário"
    )

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do produto"
    )

    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )

    categoria = models.CharField(
        max_length=60,
        blank=True,
        verbose_name="Categoria"
    )

    quantidade = models.PositiveIntegerField(
        default=0,
        verbose_name="Quantidade em estoque"
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço unitário"
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome