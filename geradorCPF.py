from random import randint

novo_cpf = ''
soma = 0

for i in range(0, 9):
    num = randint(0, 9)
    novo_cpf += str(num)

reverso = 10

for i in range(19):
    if i > 8:
        i -= 9

    soma += int(novo_cpf[i]) * reverso
    reverso -= 1

    if reverso < 2:
        reverso = 11
        d = 11 - (soma % 11)
        if d > 9:
            d = 0
        soma = 0
        novo_cpf += str(d)

print(novo_cpf)
