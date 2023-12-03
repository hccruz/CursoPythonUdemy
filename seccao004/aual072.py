# Exercícios funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# resultado = multiplica(1, 2, 3, 4, 5)
# print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def even_odd(number):
    if number % 2 == 0:
        return f"O número {number} é par!!!"
    return f"O número {number} é ímpar!!!"

resultado = even_odd(5)
print(resultado)
