"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re

cpf = input('Digite um CPF: ')

cpf_digitado = re.sub(r'[^0-9]', '', cpf)

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

print(f'O primeiro dígito é: {digito01}.')
print(f'O segundo dígito é: {digito02}.')
