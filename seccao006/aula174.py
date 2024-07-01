"""
Este módulo demonstra como trabalhar com pastas usando os e shutil em Python.
Inclui exemplos de cópia de arquivos e diretórios, exclusão de diretórios e
renomeação de arquivos.
"""

# os + shutil - Apagando e copiando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Renomear -> os.rename ou shutil.move
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

# os.unlink(NOVA_PASTA)
shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
