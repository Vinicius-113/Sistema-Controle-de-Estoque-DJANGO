from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Produto
from .forms import ProdutoForm

# Create your views here.
@login_required
def lista_produtos(request):
    produtos = Produto.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        "produtos/lista.html",
        {"produtos": produtos},
    )


@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()

            return redirect("produtos:lista")
    else:
        form = ProdutoForm()

    return render(
        request,
        "produtos/cadastro.html",
        {"form": form},
    )



@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        usuario=request.user,
    )

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            return redirect("produtos:lista")
    else:
        form = ProdutoForm(instance=produto)

    return render(
        request,
        "produtos/editar.html",
        {
            "form": form,
            "produto": produto,
        },
    )


@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        usuario=request.user,
    )

    if request.method == "POST":
        produto.delete()
        return redirect("produtos:lista")

    return render(
        request,
        "produtos/excluir.html",
        {"produto": produto},
    )

@login_required
def home(request):
    return render(request, "produtos/home.html")