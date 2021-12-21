"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Heraldo'
idade = 49
altura = 1.77
e_maior = idade > 18
peso = 90

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior?', e_maior)

imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos e seu imc é', imc)
