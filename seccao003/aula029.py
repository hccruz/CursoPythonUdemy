numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}.')
except:
    print('Isso não é um número.')
