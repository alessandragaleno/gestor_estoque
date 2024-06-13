from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome_social = models.CharField(max_length=100, verbose_name='razão social do fornecedor')
    nome_fantasia = models.CharField('nome fantasia do fornecedor')
    produtos = models.ManyToManyField('produtos.Produto', verbose_name='Produtos do Fornecedor', through='FornecedorProduto')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação do fornecedor')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data da atualização do fornecedor')

    class Meta:
        tb_table = 'fornecedores'

class FornecedorProduo(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Produto do fornecedor')
    preco = models.DecimalField(max_digits=10, decimal_place=2, verbose_name='Preço do produto')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data da atualização')

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey('produtos.Categoria', on_delete=models.CASCADE, verbose_name='categoria de produto')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação da categoria')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data da atualização da categoria')

    class Meta:
        tb_table = 'produtos'

class Categoria(models.Model):
    nome = models.CharField(max_length=100,  verbose_name='nome da categoria')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação da categoria')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data da atualização da categoria')
    unique=True

    class Meta:
        tb_table = 'categorias'

