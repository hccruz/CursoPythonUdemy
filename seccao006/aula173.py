# os + shutil - Copiando arquivos com Python
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

os.makedirs(NOVA_PASTA, exist_ok=True)

print(PASTA_ORIGINAL)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL,
                                                           NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL,
                                                         NOVA_PASTA), file_)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
