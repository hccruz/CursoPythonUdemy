# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Heraldo', 'Endereco': 'Rua Neapl, 183'},
    {'Nome': 'Reanta', 'Endereco': 'Rua Martinica, 99'},
    {'Nome': 'Giovane', 'Endereco': 'Rua Apalaches, 1612'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)

    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Heraldo', 'Rua Neapl, 183'],
#     ['Reanta', 'Rua Martinica, 99'],
#     ['Giovane', 'Rua Apalaches, 1612']
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereco']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
