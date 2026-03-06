from faker import Faker


fake = Faker()

clientes = dict()

for interado in range(10):
    clientes = {
        'cliente': fake.name,
        'dados': {
            'endereço': fake.address,
            'data_nascimento': fake.date_of_birth,
            'salario': ...
        }
    }
