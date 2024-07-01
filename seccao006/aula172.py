# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count

CAMINHO = '/media/hccruz/Arquivos/Documentos/CursoPythonUdemy/seccao005'
counter = count()


def formata_tamanho(tamanho_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado."""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for igual ou menor que 0, 0B.
    if tamanho_bytes <= 0:
        return '0B'

    # Tupla com tamanhos
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"

    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_bytes
    # com base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos.
    indice_abreviacao_tamanhos = int(math.log(tamanho_bytes, base))
    # Por enquanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamnho final
    tamanho_final = round(tamanho_bytes / potencia, 2)
    # A abreviação que queremos
    abreviacao_tamanhos = abreviacao_tamanhos[indice_abreviacao_tamanhos]

    return f'{tamanho_final} {abreviacao_tamanhos}'


print(formata_tamanho(1000))
print(formata_tamanho(1_000_000))
print(formata_tamanho(1_000_000_000_000))

for root, dirs, files in os.walk(CAMINHO):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Diretório:', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo)
        stast = os.stat(caminho_completo)
        tamanho = stast.st_size
        print('  ', the_counter, 'Arquivo:', file_, formata_tamanho(tamanho))
