# os.listdir para navegar em caminhos de arquivos
# /media/hccruz/Arquivos/Documentos/CursoPythonUdemy
import os

CAMINHO = '/media/hccruz/Arquivos/Documentos/CursoPythonUdemy'

for pasta in os.listdir(CAMINHO):
    CAMINHO_COMPLETO = os.path.join(CAMINHO, pasta)
    print(CAMINHO_COMPLETO)
    if not os.path.isdir(CAMINHO_COMPLETO):
        continue
    for item in os.listdir(CAMINHO_COMPLETO):
        print('  ', item)
