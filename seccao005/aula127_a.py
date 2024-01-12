# Exercícios - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Heraldo', 51)
p2 = Pessoa('Renata', 45)
p3 = Pessoa('Giovane', 18)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='uft8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
