# sys.argv - Executando arquivos com argumentos do sistema
# fonte = fira code (https://fonts.google.com/specimen/Fira+Code)
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passou os argumentos {argumentos[1:]}')
