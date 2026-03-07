from datetime import date
from clientes_fakes import dados_fakes


clientes = dados_fakes()


def verifica_idade(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        return 'Solicitação Negada: Menor de idade'
    else:
        return 'Maior de Idade'


def verifica_renda(renda):
    if renda <= 0:
        return 'Solicitação Negada: Renda inválida'
    elif renda <= 2500:
        return 'Solicitação Negada: Renda insuficiente'
    else:
        return 'Renda Compatível'


def verifica_perfil(idade, renda):
    if 'Negada' in idade or 'Negada' in renda:
        return 'Negado'
    else:
        return 'Perfil Inicial Aprovado para Análise'


for cliente in clientes:
    ano = cliente.get('dados').get('data_nascimento').year
    renda = cliente.get('dados').get('salario')
    status_idade = verifica_idade(ano)
    status_renda = verifica_renda(renda)
    cliente['status'] = verifica_perfil(status_idade, status_renda)

print(clientes)
