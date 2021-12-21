usuario = input('Digite seu usuario: ')
qtd_carcteres = len(usuario)

if qtd_carcteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres!')
else:
    print('Você foi cadastrado no sistema')