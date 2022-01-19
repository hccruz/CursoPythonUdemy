print('=' * 30)
print(f'{"JOGO DE ADIVINHAÇÃO!!!!":^30}')
print('=' * 30)
print()
print('Adivinhe a palavra secreta. Você terá 3 chances para acertar!!!!')

secreto = 'perfurme'
digitadas = []
chances = 3

while True:

    if chances == 0:
        print('Você perdeu!!')
        print(f'A palavra secreta era esta: {secreto}')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Ahh isso não vale, digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        chances -= 1
        print(f'Você tem {chances} chances!!!!!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

