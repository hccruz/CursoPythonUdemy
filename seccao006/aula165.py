# Maria pegou um empréstimo de 1.000.000
# para realizar o pagemtno em 5 anos
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data final do empréstimo
# - Mostre todas as datas do empréstimo e o valor dasa parcelas
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000

data_inicio = datetime.strptime('20/12/2020', '%d/%m/%Y')
data_fim = data_inicio + relativedelta(years=5)

datas_parcelas = []
data_parcela = data_inicio

while data_parcela < data_fim:
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

valor_parcela = valor_total / len(datas_parcelas)

for parcela in datas_parcelas:
    print(f'{parcela.strftime("%d/%m/%Y")}, R${valor_parcela:.2f}')

print()
print(
    f'Você pegou R${valor_total:.2f} para pagar em {len(datas_parcelas)} '
    f'parcelas de R${valor_parcela:.2f}.'
)
