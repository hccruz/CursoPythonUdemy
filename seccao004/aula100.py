# Exercícios
# Aumente  os preços dos produtos a seguir em 10%
# Gere novs_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

print('########### Novos Produtos ################')
print(*novos_produtos, sep='\n')
print()
print(*produtos,sep='\n', end='\n\n')

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(produtos,
                                     key= lambda dicionario: dicionario['nome'],
                                     reverse=True)

print('########### Produtos Ordenados por Nome ################')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos,sep='\n', end='\n\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(produtos,
                                     key= lambda dicionario: dicionario['preco'],
                                     )

print('########### Produtos Ordenados por Preço ################')
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*produtos, sep='\n')
