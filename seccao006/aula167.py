# locale para internacionalização
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/en-us/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

print(locale.getlocale())

print(calendar.calendar(2024))
