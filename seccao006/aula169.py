# os.path trabalha com caminhos em Windows, Linux e Mac
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Linux ou Mac sem precisar se preocupar com as diferenças
# entre os sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') vai retornar o caminho
# 'pasta1/pasta2/arquivo.txt' no Linux e Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho em uma tupla (diretorio, arquivo).
# Por exemplo, os.path.split ('home/user/arquivo.txt') vai retornar
# ('home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma operação
# de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo, extensao_arquivo)
print(os.path.exists('/media/hccruz/Arquivos/Documentos/CursoPythonUdemy'))
print(os.path.abspath('.'))
