# string. Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui e ignora erros se faltar chaves
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2024, 7, 3)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='55 (11) 7890-5432'
)

print(dados)

texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor no valor de ${valor} no
dia ${data}. Caso deseje cancelar o serviço, entre em contato com a ${empresa}
pelo $telefone.

Atenciosamente,

${empresa},
Abraços
'''

template = string.Template(texto)
print(template.substitute(dados))
