# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 100


if __name__ == '__main__':
    p1 = Pessoa('Heraldo', 'Cruz')
    print(p1)
