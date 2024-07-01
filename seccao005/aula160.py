# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])
as_espada = Carta('A', '♠️')
print(as_espada)
print(as_espada.naipe)
print(as_espada.valor)
print()
print(as_espada._fields)

for valor in as_espada:
    print(valor)
