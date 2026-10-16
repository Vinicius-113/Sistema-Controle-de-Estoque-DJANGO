
from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "descricao",
            "categoria",
            "quantidade",
            "preco",
        ]

        labels = {
            "nome": "Nome do produto",
            "descricao": "Descrição",
            "categoria": "Categoria",
            "quantidade": "Quantidade em estoque",
            "preco": "Preço unitário (R$)",
        }

        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex.: Teclado",
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Descreva o produto",
            }),
            "categoria": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex.: Informática",
            }),
            "quantidade": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
            }),
            "preco": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0.01",
                "step": "0.01",
            }),
        }