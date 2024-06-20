from django.db import models

from utils.base_models import BaseModel


# Create your models here.
class Local(BaseModel):
    TIPOS_DE_LOCAL = [
        ('F', 'Fisico'),
        ('D', 'Digital'),
    ]
<<<<<<< HEAD
    nome = models.CharField(
        max_length=50, verbose_name='Nome do local armazenado'
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_DE_LOCAL,
        verbose_name='Tipo do local movimentado',
    )
=======
    nome = models.CharField(max_length=50, verbose_name='Nome do local armazenado')
    tipo = models.CharField(max_length=1, choices=TIPOS_DE_LOCAL, verbose_name='Tipo do local movimentado')
>>>>>>> 6dfbba500605246f361b37a002648b0c7ec442a0

    class Meta:
        db_table = 'locais'


class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [
        ('1', 'Entrada'),
        ('-1', 'Saída'),
    ]
<<<<<<< HEAD
    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='Produto da movimentação',
    )
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=6, verbose_name='Quantidade movimentada'
    )
    fornecedor = models.ForeignKey(
        'produtos.Fornecedor',
        on_delete=models.CASCADE,
        verbose_name='Fornecedor do produto movimentado',
    )
    local = models.ForeignKey(
        'produtos.local',
        on_delete=models.CASCADE,
        verbose_name='Local de movimentação',
    )
    tipo = models.IntegerField(
    choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de movimentação'
    )
    preco = models.DecimalField(
    max_digits=10, decimal_places=6, verbose_name='Preço do produto na movimrntação'
    )
    codigo_fabricante = models.CharField(
    max_length=20, verbose_name='Código do fabricante'
    )
=======
    produto = models.ForeignKey('produtos.Produto',on_delete=models.CASCADE,verbose_name='Produto da movimentação')
    quantidade = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Quantidade movimentada')
    fornecedor = models.ForeignKey('produtos.Fornecedor', on_delete=models.CASCADE, verbose_name='Fornecedor do produto movimentado')
    local = models.ForeignKey('produtos.local', on_delete=models.CASCADE, verbose_name='Local de movimentação')
    tipo = models.IntegerField(choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de movimentação')

>>>>>>> 6dfbba500605246f361b37a002648b0c7ec442a0
    class Meta:
        db_table = 'movimentacoes'


class Embalagem(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Nome da embalagem')
    sigla = models.CharField(max_length=3, verbose_name='Sigla da embalagem')

    class Meta:
        db_table = 'embalagens'


class Fornecedor(BaseModel):
<<<<<<< HEAD
    nome_social = models.CharField(
    max_length=100, verbose_name='Razão social do fornecedor'
    )
    nome_fantasia = models.CharField(
    max_length=50, verbose_name='Nome fantasia do fornecedor'
    )
    produtos = models.ManyToManyField(
    'produtos.Produto',
    verbose_name='Produtos do Fornecedor',
    )
=======
    nome_social = models.CharField(max_length=100, verbose_name='Razão social do fornecedor')
    nome_fantasia = models.CharField(max_length=50, verbose_name='Nome fantasia do fornecedor')
    produtos = models.ManyToManyField('produtos.Produto', verbose_name='Produtos do Fornecedor')
>>>>>>> 6dfbba500605246f361b37a002648b0c7ec442a0

    class Meta:
        db_table = 'fornecedores'

<<<<<<< HEAD
=======
class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='Nome do produto')
    categoria = models.ForeignKey('produtos.Categoria', on_delete=models.CASCADE, verbose_name='categoria de produto')
    embalagens = models.ManyToManyField('produtos.Embalagem', verbose_name='Embalagem do produto')
>>>>>>> 6dfbba500605246f361b37a002648b0c7ec442a0

class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='Nome do produto')
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='Categoria de produto',
    )
    embalagens = models.ManyToManyField(
        'produtos.Embalagem', verbose_name='Embalagem do produto'
    )
    estoque_minimo = models.FloatField(
    verbose_name='Estoque mínimo do produto',
    )
    estoque_maximo = models.FloatField(
    verbose_name=
        'Estoque máximo do produto',
    )
    class Meta:
        db_table = 'produtos'


class Categoria(BaseModel):
<<<<<<< HEAD
    nome = models.CharField(max_length=100, verbose_name='ome da categoria')
    unique = True
=======
    nome = models.CharField(max_length=100, verbose_name='Nome da categoria')
    unique=True
>>>>>>> 6dfbba500605246f361b37a002648b0c7ec442a0

    class Meta:
        db_table = 'categorias'
