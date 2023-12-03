# Exercícios
# Crie funções qu duplicam, triplicam e quadruplicam o número recebido
# como parâmetro

def criar_multiplicador(multiplicador):
    def multiplicar(number):
        return f'{number} x {multiplicador} = {number * multiplicador}'
    return multiplicar

resultado = criar_multiplicador(5)

print(resultado(4))
