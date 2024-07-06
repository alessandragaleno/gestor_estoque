from django.urls import path

from .views import (
    adicionar_categoria,
    adicionar_embalagem,
    adicionar_local,
    editar_categoria,
    editar_embalagem,
    editar_local,
    excluir_categoria,
    excluir_embalagem,
    excluir_local,
    inicio,
    listar_categoria,
    listar_embalagem,
    listar_locais,
)

urlpatterns = [
    # locais
    path('', inicio, name='inicio'),
    path('locais/', listar_locais, name='listar_locais'),  # noqa: F821
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('locais/editar/<int:pk>/', editar_local, name='editar_local'),  # noqa: F821 # type: ignore
    path('locais/excluirr/<int:pk>/', excluir_local, name='excluir_local'),  # type: ignore  # noqa: F821
    # embalagens
    path('embalagens/', listar_embalagem, name='listar_embalagens'),  # noqa: F821
    path('embalagens/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),  # noqa: E501
    path('embalagens/editar/<int:pk>/', editar_embalagem, name='editar_embalagem'),  # noqa: F821 , E501# type: ignore
    path('embalagens/excluir/<int:pk>/', excluir_embalagem, name='excluir_embalagem'),  # type: ignore  # noqa: F821, E501
    # categorias
    path('categorias/', listar_categoria, name='listar_categorias'),  # noqa: F821
    path('categorias/adicionar/', adicionar_categoria, name='adicionar_categoria'),  # noqa: E501
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),  # noqa: E501
    path('categorias/excluir/<it:pk>/', excluir_categoria, name='excluir_categoria')  # noqa: E501
]
