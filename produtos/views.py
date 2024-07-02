from django.shortcuts import redirect, render

from .forms import LocalForm
from .models import Local


def inicio(request):
    return render(request, 'index.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()  # noqa: F821
    if consulta:
        locais = locais.filter(nome_icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})  # noqa: E501


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            return redirect('listar_locais')  # noqa: E112
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def editar_local(request):
    return render(request, 'produtos/editar_locais.html')


def excluir_local(request):
    return render(request, 'produtos/excluir_locais.html')


def listar_embalagem(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()  # noqa: F821
    if consulta:
        locais = locais.filter(nome_icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_embalagem.html', {'locais': locais})  # noqa: E501


def adicionar_embalagem(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            return redirect('listar_embalagem')  # noqa: E112
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})  # noqa: E501
