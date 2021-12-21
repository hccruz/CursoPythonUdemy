"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom Dia: 0 - 11, Boa Tarde: 12 -17 e Boa Noite: 18 - 23.
"""
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


hora = input('Digite uma hora inteira: ')

if is_int(hora):
    hora = int(hora)
    if hora < 0 or hora >= 24:
        print('Por favor, digite um horário entre 0 e 23.')
    elif hora <= 11:
        print('Bom Dia!!!')
    elif hora <= 17:
        print('Boa Tarde!!!')
    else:
        print('Boa Noite!!!')
else:
    print('Você digitou um valor NÃO VÁLIDO para hora. \nDigite somente valores INTEIROS de hora!!!')
