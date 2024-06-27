from django.urls import path

from .views import adicionar_local, inicio, listar_locais

urlpatterns = [
    path('', inicio, name='inicio'),
    #locais
    path('locais/', listar_locais, name='listar_locais'),  # noqa: F821
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    #path('locais/editar/<int:pk>/', editar_local, name='editar_local'),
    #path('locais/excluirr/<int:pk>/', excluir_local, name='excluir_local'),

]
