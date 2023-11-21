cpf = input('Digite um número de 9 dígitos: ')

contador = 10
total = 0

for numero in cpf:
    total += int(numero) * contador
    contador -= 1

digito01 = (total * 10) % 11

if digito01 > 9:
    digito01 = 0

total = 0
contador = 11

cpf_digito01 = cpf + str(digito01)

for numero in cpf_digito01:
    total += int(numero) * contador
    contador -= 1

digito02 = (total * 10) % 11

if digito02 > 9:
    digito02 = 0

cpf_gerado = f'{cpf}{digito01}{digito02}'

print(f'{cpf_gerado}')
