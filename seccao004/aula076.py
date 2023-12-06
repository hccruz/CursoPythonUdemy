# Exercício - Sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opcao': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5',
        'Opcao': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opcao': ['4', '5', '2', '1'],
        'Resposta': '5'
    }
]

resposta_certa = 0

for indice, per in enumerate(perguntas):
    print(f"Pergunta: {per['Pergunta']}\n")
    print("Opções:")
    for ind, op in enumerate(per['Opcao']):
        print(f"{ind}) {op}")
    resposta = input('Escolha uma opção: ')
    try:
        condicao = per['Resposta'] == per['Opcao'][int(resposta)]
        if condicao:
            print('Acertou!!!\n')
            resposta_certa += 1
        else:
            print('Errou!!!\n')
    except ValueError:
        print('Errou!!!\n')
    except IndexError:
        print('Errou!!!\n')

print(f"Você acertou {resposta_certa} de 3 perguntas.")
