"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''numero_str = input('Digite um numero: ')

if numero_str.isdigit():
    e_numero = int(numero_str) % 2 == 0
    if e_numero:
        print(f'O número digitado {numero_str} é par.')
    else:
        print(f'O número digitado {numero_str} é ímpar.')
else:
    print(f'O número digitado {numero_str} não é um número inteiro.')'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''hora_str = input('Digite um hora interia: ')

if hora_str.isdigit():
    hora_int = int(hora_str)
    if hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!!')
    else:
        print('Esta hora não existe!!')
else:
    print('Digite um valor inteiro para a hora.')'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto."; se tiver entre 5 e 6 letras, escreva
"Seu nome é noraml."; maior que 6 "Seu nome é muito grande.".
"""

'''nome = input('Digite o seu nome: ')

letras = len(nome)

if letras <= 4:
    print('Seu nome é curto.')
elif letras >= 5 and letras <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')'''
