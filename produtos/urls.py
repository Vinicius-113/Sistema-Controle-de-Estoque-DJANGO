
from django.urls import path
from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.lista_produtos, name="lista"),
    path("produtos/novo/", views.cadastrar_produto, name="cadastrar"),
    path(
        "produtos/<int:produto_id>/editar/",
        views.editar_produto,
        name="editar",
    ),
    path(
        "produtos/<int:produto_id>/excluir/",
        views.excluir_produto,
        name="excluir",
    ),
]
