# os.walk
# os.walk é uma função permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

CAMINHO = '/media/hccruz/Arquivos/Documentos/CursoPythonUdemy/seccao005'
counter = count()

for root, dirs, files in os.walk(CAMINHO):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Diretório:', dir_)

    for file_ in files:
        print('  ', the_counter, 'Arquivo:', file_)
