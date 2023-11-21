import re
import sys

cpf = input('Digite um CPF: ')

cpf_digitado = re.sub(r'[^0-9]', '', cpf)

cpf_eh_sequencia = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)

if cpf_eh_sequencia:
    print('Você enviou dados sequenciais.')
    sys.exit()

contador = 10
total = 0

for numero in cpf_digitado[:9]:
    total += int(numero) * contador
    contador -= 1

digito01 = (total * 10) % 11

if digito01 > 9:
    digito01 = 0

total = 0
contador = 11

for numero in cpf_digitado[:10]:
    total += int(numero) * contador
    contador -= 1

digito02 = (total * 10) % 11

if digito02 > 9:
    digito02 = 0

cpf_gerado = f'{cpf_digitado[:9]}{digito01}{digito02}'

if cpf_digitado == cpf_gerado:
    print(f'O CPF {cpf_gerado} é válido.')
else:
    print(f'O CPF {cpf_gerado} é inválido.')
