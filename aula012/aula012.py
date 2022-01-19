"""
Formatando valores com modificadores - Aula 012

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print(f'{divisao:.2f}')

nome = 'Heraldo Cruz'
nome_formatado = f'{nome:@>50}'
print(nome_formatado)

# print(len(nome))

# print(f'{nome:#^50}')
