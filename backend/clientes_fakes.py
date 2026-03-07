from faker import Faker
from random import randint


def dados_fakes():
    fake = Faker('pt_BR')
    clientes = []
    for identificador in range(10):
        clientes.append({
            'id': identificador,
            'cliente': fake.name(),
            'dados': {
                'endereço': fake.address(),
                'data_nascimento': fake.date_of_birth(),
                'salario': float(randint(1300, 20000))
            }
        })
    return clientes
