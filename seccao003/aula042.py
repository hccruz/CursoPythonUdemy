frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'

i = 0
qtd_letras = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letras_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letras < qtd_letras_atual:
        qtd_letras = qtd_letras_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes.upper()}" que apareceu '
      f'{qtd_letras}x')
