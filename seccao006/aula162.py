# Criando datas com módulo datetime
# datetime (ano, mês, dia)
# datetime (ano, mês, dia, hora, minuto, segundo)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/2/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

# data_str = '2024-04-20 07:49:23'
# data_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2024, 4, 20, 7, 49, 20)
# data = datetime.strptime(data_str, data_fmt)

data = datetime.now()

print(data.timestamp())
print(data.fromtimestamp(1716999758))
