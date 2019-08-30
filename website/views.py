from django.shortcuts import render
from website.models import Pessoa, Ong

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

 
    return render(request, 'index.html')


def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto)


def cadastrar_ong(request):
    if request.method == 'POST':
        x = Ong()
        x.nome_responsavel = request.POST.get('nome_responsavel')
        x.nome = request.POST.get('nome')
        x.email = request.POST.get('email')
        x.str_cep = request.POST.get('str_cep')
        x.str_numero = request.POST.get('str_numero')
        x.complemento = request.POST.get('complemento')
        x.telefone = request.POST.get('telefone')
        x.horario_funcionamento = request.POST.get('horario_funcionamento')
        x.observacao = request.POST.get('observacao')
        x.save()

        contexto = {'msg': 'Parabéns ' + x.nome}
        return render(request, 'sucesso.html', contexto)


    return render(request, 'cadastrar-ong.html')