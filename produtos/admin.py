from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "quantidade",
        "preco",
        "usuario",
    )

    search_fields = ("nome", "categoria")
    list_filter = ("categoria",)