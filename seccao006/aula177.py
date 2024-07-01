# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
)

filme = {
        'title': 'Senhor do Anéis: A Sociedade do Anel',
        'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
        'is_movie': True,
        'imdb_rating': 8.8,
        'year': 2001,
        'characters': ['Frodo', 'Sam', 'Gandolf', 'Legolas', 'Bormir'],
        'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, indent=4, ensure_ascii=False)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_lido = json.load(arquivo)
    print(filme_lido)
