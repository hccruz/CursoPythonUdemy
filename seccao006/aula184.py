# Variavéis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env variável = valor | dir env:
# Linux e Mac: export variável=valor | echo variável
# Para obter o valor das variáveis de ambiente
# os.getenv(variável) ou os.environ[variável]
# Para configurar as variáveis de ambiente
# os.environ[variável] = valor
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# OBS.: sempre lembre-se de criar um arquivo .env-example
import os
from dotenv import load_dotenv

load_dotenv()

# print(os.environ)

print(os.getenv('BD_PASSWORD'))
