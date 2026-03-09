from datetime import date
from random import randint
from clientes_fakes import dados_fakes


clientes = dados_fakes()


def verificar_intervalo_idade(idade):
    if 18 <= idade <= 65:
        return 'Idade compatível.'
    else:
        return 'Solicitação Negada: Cliente não atende os requisitos de idade.'


def verificar_comprometimento_renda(salario, parcela):
    if parcela > salario * 0.3:
        return 'Solicitação Negada: Cliente não atende os requisitos de renda.'
    else:
        return 'Renda compatível.'


def calcular_parcela(valor_emprestimo, taxa_juros, num_parcelas):
    """
    Calcula o valor da parcela fixa de um empréstimo.

    :param valor_emprestimo: Valor total do empréstimo (PV)
    :param taxa_juros: Taxa de juros por período (ex.: 0.02 para 2% ao mês)
    :param num_parcelas: Número total de parcelas (n)
    :return: Valor da parcela (PMT)
    """
    # Validações básicas
    if valor_emprestimo <= 0:
        raise ValueError("O valor do empréstimo deve ser maior que zero.")
    if taxa_juros < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")
    if num_parcelas <= 0:
        raise ValueError("O número de parcelas deve ser maior que zero.")

    # Fórmula da Tabela Price
    if taxa_juros == 0:
        # Caso especial: juros zero → parcelas iguais ao valor dividido pelo número de parcelas
        return valor_emprestimo / num_parcelas

    pmt = (valor_emprestimo * taxa_juros) / (1 - (1 + taxa_juros) ** (-num_parcelas))
    return pmt


for cliente in clientes:
    ano = cliente.get('dados').get('data_nascimento').year
    renda = cliente.get('dados').get('salario')
    idade = date.today().year - ano
    status_idade = verificar_intervalo_idade(idade)
    valor_solicitado = float(randint(1000, 5000))
    cliente['valor_solicitado'] = valor_solicitado
    juros = randint(1, 3) / 100
    cliente['juros'] = juros
    num_parcela = randint(24, 60)
    cliente['número de parcelas'] = num_parcela
    parcelas = round(calcular_parcela(valor_solicitado, juros, num_parcela), 2)
    cliente['parcelas'] = parcelas
    status_renda = verificar_comprometimento_renda(renda, parcelas)
    if 'Negada' in status_idade or 'Negada' in status_renda:
        cliente['status_solicitação'] = 'Solicitação Negada: Cliente não atende os requisitos.'
    else:
        cliente['status_solicitação'] = 'Solicitação Aprovada'
    print(cliente)
