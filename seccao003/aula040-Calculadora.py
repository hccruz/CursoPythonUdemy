'''Calculadora com while'''

while True:
    # Informe os números e o operador para realizar o cálculo
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador aritmético (+-/*): ')

    # Definir uma variável para verificar os números
    numeros_validos = None

    # Atribuir valores para as variáveis de ponto flutuante
    num_1_float = 0
    num_2_float = 0

    # Transformar os números textos em números de ponto flututante
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # Validar os números
    if numeros_validos is None:
        print('Um ou amobos números digitados são inválidos.')
        continue

    # Definir uma variável para verificar os operadores
    operadores_permitidos = '+-*/'

    # Validar os operadores
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    # Validar se foi digitado somente um operador
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # Realizar os cálculos
    if operador == '+':
        print(f'{num_1_float} {operador} {num_2_float} = ' +
              f'{num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} {operador} {num_2_float} = ' +
              f'{num_1_float - num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} {operador} {num_2_float} = ' +
              f'{num_1_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} {operador} {num_2_float} = ' +
              f'{num_1_float / num_2_float}')

    # Definir uma variável para sair do loop
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    # Verificar se a variável de saída é verdadeira
    if sair:
        break
