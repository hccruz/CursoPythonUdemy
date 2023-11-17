"""
Faça um jogo para o usuário advinhar a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
# Importar bibliotecas
import os

# Definir a variável palavra encontrada
palavra_encontrada = ''

# Atribuir a palavra secreta
palavra_secreta = 'perfume'

# Encontrar tamanho da palavra secreta
tamanho_palavra_secreta = len(palavra_secreta)

# Definir a variável palavra formatada
palavra_formatada = '*' * tamanho_palavra_secreta

# Definir contador de tentativas
contador = 0

# Loop para encontrar a palavra secreta
while True:
    # Entrada para descobrir a palavra secreta
    letra_digitada = input('Digite uma letra: ').lower()

    # Validar se foi digitado somente uma letra
    if len(letra_digitada) > 1:
        print('Digite somente uma letra.')
        continue

    # Validar se a entrada para somente letras
    if letra_digitada.isdigit():
        print('Você tem que digitar uma letra e não um número.')
        continue

    # Procurar a letra digitada na palavra secreta
    for i in range(tamanho_palavra_secreta):
        if palavra_secreta[i] == letra_digitada:
            palavra_encontrada += letra_digitada
        else:
            palavra_encontrada += palavra_formatada[i]

    # Atribuir palavra encontrada para palavra formatada
    palavra_formatada = palavra_encontrada
    palavra_encontrada = ''  # Limpar palavra encontrada

    # Incrementar contador
    contador += 1

    print(palavra_formatada)  # Imprimir a palavra formatada

    # Imprimir ao usuário resultado do jogo
    if palavra_formatada == palavra_secreta:
        os.system('cls')  # Limpar tela do computador
        print('VOCÊ GANHOU!!!! PARABÉNS!!!')
        print(f'A palavara secreta é {palavra_formatada} e você utilizou ' +
              f'{contador} tentativas.')
        break  # Saída do programa
