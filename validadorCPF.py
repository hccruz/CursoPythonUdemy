cpf = input('Digite o CPF sem traço e pontos: ')
soma = 0

for p, r in enumerate(range(10, 1, -1)):
    soma += int(cpf[p]) * r

res1 = 11 - (soma % 11)

if res1 > 9:
    digito1 = 0
else:
    digito1 = res1

for p, r in enumerate(range(11, 1, -1)):
    soma += int(cpf[p]) * r

res2 = 11 - (soma % 11)

if res2 > 9:
    digito2 = 0
else:
    digito2 = res2

novo_cpf = cpf[0:9] + str(digito1) + str(digito2)

if cpf == novo_cpf:
    print('CPF é válido!!!!')
else:
    print('CPF é inválido!!!')
