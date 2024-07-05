from django.shortcuts import get_object_or_404, redirect, render  # noqa: I001

from .forms import LocalForm, EmbalagemForm
from .models import Embalagem, Local



def inicio(request):  # noqa: E303
    return render(request, 'index.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()  # noqa: F821
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
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


def editar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return render(request, 'listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def excluir_local(request):
    local = get_object_or_404(Local, pk=pk)  # type: ignore # noqa: F821
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.delete()
            return render(request, 'listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/exclusao_locais.html', {'local': local})


def listar_embalagem(request):
    consulta = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()  # noqa: F821
    if consulta:
        embalagens = embalagens.filter(nome_icontains=consulta)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagem.html', {'embalagens': embalagens})  # noqa: E501


def adicionar_embalagem(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')  # noqa: E112
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})  # noqa: E501


def editar_embalagem(request, pk):  # noqa: F811
    local = get_object_or_404(Embalagem, pk=pk)  # noqa: E111
    if request.method == 'POST':  # noqa: E113
        form = LocalForm(request.POST, instance=Embalagem)
        if form.is_valid():
            form.save()
            return render(request, 'listar_embalagem')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})


def excluir_embalagem(request, pk):  # noqa: E303
    local = get_object_or_404(Embalagem, pk=pk)  # noqa:
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=Embalagem)
        if form.is_valid():
            form.delete()
            return render(request, 'excluir_local')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/exclusao_embalagem.html', {'form': form})
