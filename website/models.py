from django.db import models
import datetime

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
    )
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=50,
        verbose_name='Sobrenome'
    )
    data_nascimento = models.DateField(
        verbose_name = 'Data de Nascimento'
    )
    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )
    str_cep = models.CharField(
        max_length=10,
        verbose_name='CEP'
    )
    str_numero = models.CharField(
        max_length=5,
        verbose_name='Número Res.'
    )
    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento',
        null=True,
        blank=True
    )
    genero = models.CharField(
        choices=GENEROS,
        max_length=255,
        verbose_name='Gênero'
    )

    telefone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Telefone'
    ) 

    celular = models.CharField(
        max_length=255,
        verbose_name='Celular'
    ) 

    motivo = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
       return self.nome + ' ' + self.sobrenome


class Ong(models.Model):
    nome_responsavel = models.CharField(
        max_length=255,
        verbose_name='Nome Responsável'
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True,
        default=''
    )

    str_cep = models.CharField(
        max_length=10,
        verbose_name='CEP'
    )

    str_numero = models.CharField(
        max_length=5,
        verbose_name='Número Res.'
    )

    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento',
        null=True,
        blank=True
    )

    telefone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Telefone'
    )

    horario_funcionamento = models.TextField()

    observacao = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome + ' --- ' + self.nome_responsavel

class Pet(models.Model):
    PORTE = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    raca = models.CharField(
        max_length=255,
        verbose_name='Raça'
    )
    porte = models.CharField(
        max_length=255,
        verbose_name='Porte',
        choices=PORTE
    )
    peso = models.FloatField(
        verbose_name = 'Peso'
    )

    dono = models.ForeignKey(Pessoa,
        on_delete=None
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome + ' --- ' + self.dono.email
