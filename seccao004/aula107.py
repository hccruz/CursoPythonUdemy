# Exercícios - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas lista na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     intervalo_minimo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_minimo)
#     ]
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
      
print(*list(zip(l1, l2)), sep='\n')
print()
print(*list(zip_longest(l1, l2)), sep='\n')
