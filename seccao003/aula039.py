'''
Iterando strings com while
'''

nome = 'Heraldo Candido'  # Iteráveis
tamanho_nome = len(nome)

contador = 0
novo_nome = ''

while contador < tamanho_nome:
    novo_nome += '*' + nome[contador]
    contador += 1

print(novo_nome)
