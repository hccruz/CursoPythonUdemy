from pathlib import Path

CAMINHO_PROJETO = Path()
# print(CAMINHO_PROJETO.absolute())

CAMINHO_ARQUIVO = Path(__file__)
# print(CAMINHO_ARQUIVO)

ideias = CAMINHO_ARQUIVO.parent / 'ideias'
# print(ideias / 'arquivo.txt')

arquivo = CAMINHO_ARQUIVO.parent / 'arquivo.txt'
arquivo.touch()

print(arquivo)
arquivo.write_text('Olá mundo')
print(arquivo.read_text())
arquivo.unlink()

caminho_arquivo = CAMINHO_ARQUIVO.parent / 'arquivo.txt'

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\r\n')
    file.write('Outra linha\r\n')

print(caminho_arquivo.read_text())
caminho_arquivo.unlink()
