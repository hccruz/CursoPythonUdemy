"""
Faça uma lista de comprar com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
lista_compras = []

while True:
    opcao = input('Selecione uma opção \n' +
                  '[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        item = input('Digite um item para comprar: ')
        lista_compras.append(item)
    elif opcao == 'a':
        try:
            indice = input('Digite o indice do item para apagar: ')
            lista_compras.pop(int(indice))
        except ValueError:
            print('Digite somente números.')
        except IndexError:
            print('Índice não existe na lista.')
    elif opcao == 'l':
        if len(lista_compras) > 0:
            for i, nome in enumerate(lista_compras):
                print(i, nome)
        else:
            print('Não existe itens na lista.')
    else:
        print('Por favor digite i, a ou l.')
